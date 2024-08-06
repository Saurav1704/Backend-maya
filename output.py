#import standard libraries
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, AgGridTheme

#import local files
from generate import generate_response
from database import read_sql_query
# from database import get_data_from_service
import plotly.express as px

user_icon = 'icon.png'
assistant_icon = 'ai.jpg'

def show_history(st):
    #load all the stored chat history
        if len(st.session_state.messages) > 0:
            for message in st.session_state.messages:
                role = message.get('role')
                avatar = message.get('avatar', assistant_icon if role == 'assistant' else user_icon)
                if message.get('data') == None:
                    response_df = pd.DataFrame()
                else:
                    response_df = pd.DataFrame(message['data'])
                show_assistant_message(st , role  , avatar  , response_md = message['content']  , response_df = response_df  ) 



def show_output(st , question):
        #load all the stored chat history
        if len(st.session_state.messages) > 0:
            for message in st.session_state.messages:
                role = message.get('role')
                avatar = message.get('avatar', assistant_icon if role == 'assistant' else user_icon)
                if message.get('data') == None:
                    response_df = pd.DataFrame()
                else:
                    response_df = pd.DataFrame(message['data'])
                show_assistant_message(st , role  , avatar  , response_md = message['content']  , response_df = response_df  )
        st.session_state.messages.append({'role': 'user', 'content': question})
        with st.chat_message('user', avatar=user_icon):
            st.markdown(question)  
        response_df = pd.DataFrame()
        # service =  generate_response(question)
        response_md = generate_response(question)  
        #if we did'nt get get select query in response text then we will fetch data
        if question.lower() in ["hello", "hi", "who are you"]:
            message = {'role': "assistant", 'content': response_md }
            st.session_state.messages.append(message)
            with st.chat_message("assistant", avatar= assistant_icon):
                st.markdown(message['content'])
                exit()
        else:
        # Generate AI response
            try:
                query_result, column_names  = read_sql_query(response_md)
                response_df = pd.DataFrame(query_result, columns=column_names)
                # service_data , error = get_data_from_service(service) 
                # response_df = pd.DataFrame(service_data)
            except Exception as e:
                error = str(e)
                message = {'role': "assistant", 'content': error}
                st.session_state.messages.append(message)
                show_assistant_message(st ,role='assistant', avatar= assistant_icon,  response_md = error)
                exit()
        # Add AI message to chat history with DataFrame if available
        # message = {'role': "assistant", 'content': service_data}
        message = {'role': "assistant", 'content': response_md}
        if not response_df.empty:
            message['data'] = response_df.to_dict()  # Convert DataFrame to dict for storage
        st.session_state.messages.append(message)
        show_assistant_message(st , role='assistant', avatar= assistant_icon , response_md  = response_md, response_df = response_df)
        # Display AI message in chat
def show_assistant_message( st  , role , avatar  , response_md , response_df = pd.DataFrame()):
        if role == "user":
             with st.chat_message(role , avatar = avatar):
                 st.markdown(response_md)
        else:
            with st.chat_message("assistant", avatar = avatar):
                if not response_df.empty:
                    tab1, tab2 = st.tabs(["Tabular Data", "Graphical Representation"])
                    with tab1:
                        # Configure AgGrid options
                        try:
                            gb = GridOptionsBuilder.from_dataframe(response_df)
                            gb.configure_pagination(paginationPageSize=10)
                            gb.configure_default_column()
                            grid_options = gb.build()
                            grid_response = AgGrid(
                                response_df,
                                gridOptions=grid_options,
                                enable_enterprise_modules=True,
                                theme=AgGridTheme.STREAMLIT,
                                fit_columns_on_grid_load=True,
                                update_mode='MODEL_CHANGED'
                            )
                        except:
                            st.markdown("Data is already displayed. Please refer above")
                            return()
 
                        del gb
                        paginated_data = pd.DataFrame(grid_response['data'])
                    with tab2:
                        if len(paginated_data.columns) == 2 and paginated_data.dtypes[1] in ['int64', 'float64'] or st.session_state.load_data:
                            st.session_state.load_data = True
                            # User input for graph type selection
                            # graph_type = st.radio("Select graph type:", ["Bar Graph", "Line Plot", "Histogram"])
                            # graphs = ["Bar Graph", "Line Plot", "Histogram"]

                            
                            graphs = st.selectbox("Select Chart:", ["Bar Graph", "Line Plot", "Histogram"])
            
                            x_data = paginated_data[paginated_data.columns[0]]
                            y_data = paginated_data[paginated_data.columns[1]]
                            
                            if graphs == "Bar Graph":
                                st.session_state.graph_type = "Bar Graph"
                                st.bar_chart(data=paginated_data.set_index(paginated_data.columns[0]))

                            elif graphs == "Line Plot":
                                st.session_state.graph_type = "Line Plot"
                                fig = px.line(paginated_data, x=x_data, y=y_data, title=f'Line Chart of {paginated_data.columns[1]}')
                                st.plotly_chart(fig, use_container_width=True)

                            elif graphs == "Histogram":
                                st.session_state.graph_type = "Histogram"
                                hist_data = paginated_data[paginated_data.columns[1]]
                                hist_label = paginated_data.columns[1]
        
                                fig = px.histogram(paginated_data, x=hist_data, title=f'Histogram of {hist_label}')
                                st.plotly_chart(fig, use_container_width=True)
                            
                        else:
                            st.markdown("The data is not suitable for a Bar chart.")
                            return
                else:
                    st.markdown(response_md)