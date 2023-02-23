# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import warnings

import leafmap as leafmap

warnings.simplefilter(action='ignore', category=FutureWarning)
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_card import card
import streamlit_tags
from streamlit_option_menu import option_menu
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, AgGridTheme
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
import altair as alt
import matplotlib.pyplot as plt
import pydeck as pdk
import leafmap.foliumap as leafmap
import altair as alt
from vega_datasets import data

st.set_page_config(layout="wide")
# Firebase Authentication

st.title('Tableau de bord de gestion et d\'analyse des données')
st.markdown("***********")

with st.sidebar:
    selected = option_menu("Main Menu", ["Home",
                                       #  'Projects',
                                         # 'Members',
                                         'Data',
                                         'About',
                                         # 'Settings'
                                         ],
                           icons=['house', 'kanban', 'info-square','list-task', 'info-square', 'people', 'list-task',
                                  'gear'], menu_icon="cast",
                           default_index=0)
if selected == 'Home':
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [48.85, 2.35],
        columns=['lat', 'lon'])
    st.map(df)
    data_frame = pd.read_excel('data.xlsx')
    data_frame = data_frame[data_frame['No de compte'].notna()]

    source = data_frame[['No de compte', 'Nbre de livraison', 'Solution']]  # data.cars()

    chart = alt.Chart(source, height=500).mark_bar().encode(
        x='No de compte',
        y='Nbre de livraison',
        color='Solution',
    ).interactive()
    st.altair_chart(chart, theme="streamlit", use_container_width=True)

    source_2 = data_frame[['No de compte', 'DPT', 'Solution']]  # data.cars()

    chart_2 = alt.Chart(source_2, height=800).mark_point().encode(
        x='No de compte',
        y='DPT',
        color='Solution',
    ).properties(title='data').interactive()
    st.altair_chart(chart_2, theme="streamlit", use_container_width=True)

    #
    # m = leafmap.Map(center=[48.85, 2.35], zoom=4)
    # cities = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
    # regions = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson'
    #
    # m.add_geojson(regions, layer_name='US Regions')
    # m.add_points_from_xy(
    #     cities,
    #     x="longitude",
    #     y="latitude",
    #     color_column='region',
    #     icon_names=['gear', 'map', 'leaf', 'globe'],
    #     spin=True,
    #     add_legend=True,
    # )
    #
    # m.to_streamlit(height=700)

# if selected == 'Members':
#     st.markdown(
#         f'<p style="background-color:#ffffff;color:#fcba03;font-size:34px;font-weight:bold;border-radius:2%;">Our Team</p>',
#         unsafe_allow_html=True)
#
#     team_menu = option_menu(None, ["All Team", "New Member", "Statistics", 'Settings'],
#                             icons=['house', 'person-plus', "graph-up-arrow", 'gear'],
#                             menu_icon="cast", default_index=0, orientation="horizontal")
#
#     if team_menu == 'All Team':
#         print('all Team')
#
#     if team_menu == 'New Member':
#         full_name = st.text_input('Full Name')
#         email = st.text_input('Email')
#         roles = streamlit_tags.st_tags(
#             label='',
#             text='Press enter to add more',
#             value=['Full stack developer'],
#             suggestions=['Manager', 'DevOps', 'Backend Developer',
#                          'Frontend Developer', 'UI/UX', 'Marketing Manager',
#                          'Team Manager', 'Mobile Full stack', 'Data Scientist'],
#             maxtags=4,
#             key='1')
#         validate = st.button('Add Member', type='primary')


# if selected == 'Projects':
#     st.markdown(
#         f'<p style="background-color:#ffffff;color:#fcba03;font-size:34px;font-weight:bold;border-radius:2%;">Our Projects</p>',
#         unsafe_allow_html=True)
#     team_menu = option_menu(None, ["All Projects", "New Project", "Statistics", 'Settings'],
#                             icons=['house', 'plus-circle-dotted', "graph-up-arrow", 'gear'],
#                             menu_icon="cast", default_index=0, orientation="horizontal")
#
#     if team_menu == 'All Projects':
#         print('All Projects')
#
#
#
#     if team_menu == 'New Project':
#         title = st.text_input('Project Title')
#         client = st.text_input('Client Name')
#         client_email = st.text_input('Client Email')
#         about_project = st.text_input('About Project')
#         time = st.number_input('Estimated Time in days', step=1)
#         start_date = st.date_input(label='starting date')
#
#         validate = st.button('Add Project', type='primary')
#         if validate:
#             project_data = {
#                 "title": title,
#                 "client name": client,
#                 "client email": client_email,
#                 "about project": about_project,
#                 "time": time,
#                 "start date": str(start_date)
#             }
#             # db.child('projects').child(id).child("full name").set(title)
#             # db.child('projects').child(id).child("client name").set(client)
#
#             st.info('Project added successfully')

if selected == 'Data':
    st.markdown(f'<p style="background-color:#ffffff;color:#fcba03;font-size:34px;font-weight:bold;border-radius:2'
                f'%;">Tasks</p>',
                unsafe_allow_html=True)

    task_menu = option_menu(None, ["All Data", "New Entry", "Statistics"],
                            icons=['house', 'database-add', "graph-up-arrow", 'gear'],
                            menu_icon="cast", default_index=0, orientation="horizontal")

    if task_menu == 'All Data':
        df = pd.read_excel('data.xlsx')  # pd.DataFrame(tasks.val()).T
        # df.reset_index(drop=True, inplace=True)
        # df = df.reindex(columns=['task date', 'From time', 'To time', 'developer', 'project', 'task comment', 'task '
        #                                                                                                  'link',
        #                         'task code', 'tags'])
        # df.to_csv('df.csv', sep=',', encoding='-utf-8')

        # st.dataframe(df)
        # AgGrid(df)

        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_pagination(paginationAutoPageSize=True)  # Add pagination
        gb.configure_side_bar()  # Add a sidebar
        gb.configure_selection('multiple', use_checkbox=True,
                               groupSelectsChildren="Group checkbox select children")  # Enable multi-row selection
        gridOptions = gb.build()
        indexes = [index for index in df.index]
        selected_index = []

        grid_response = AgGrid(
            df,

            gridOptions=gridOptions,
            data_return_mode=DataReturnMode.AS_INPUT,
            update_mode=GridUpdateMode.SELECTION_CHANGED,
            fit_columns_on_grid_load=False,
            theme='alpine',  # Add theme color to the table
            enable_enterprise_modules=True,
            height=850,
            width='100%',
            reload_data=False
        )

        data = grid_response['data']
        selected = grid_response['selected_rows']

        # mapdata = df[['']]
        # st.map()

    if task_menu == 'New Task':
        projects = st.selectbox('Select Project', ['A', 'B', 'C'])
        developer = st.selectbox('Select Developer', ['A', 'B', 'C'])
        task_code = st.text_input('Task Code')
        task_link = st.text_input('Task Link')
        task_date = st.date_input(label='Task Date')
        task_from_time = st.time_input(label='From')
        task_to_time = st.time_input(label='To')
        task_comment = st.text_area('Comment')
        tags = streamlit_tags.st_tags(
            label='',
            text='Press enter to add more',
            value=['backend'],
            suggestions=['backend', 'frontend', 'mobile', 'other'],
            maxtags=4,
            key='1')
        validate = st.button('Add Task', type='primary')

        if validate:
            task_data = {
                "project": projects,
                "developer": developer,
                "task code": task_code,
                "task link": task_link,
                "task date": str(task_date),
                "From time": str(task_from_time),
                "To time": str(task_to_time),
                "task comment": str(task_comment),

                "tags": tags,

            }

            st.info('Task added successfully')

    if task_menu == 'Statistics':
        # d = pd.read_csv('df.csv', on_bad_lines='skip')
        df = pd.read_excel('data.xlsx')

        # # d["date"] = pd.to_datetime(d.date).dt.date
        # # d['date'] = pd.DatetimeIndex(d.date)
        # df = d.loc[:, ~d.columns.str.contains('^Unnamed')]
        #
        # # df = pd.read_clipboard()
        # df1 = df.reset_index().melt(id_vars='index')
        # chart = alt.Chart(df[['project', 'developer']]).mark_bar().encode(
        #     x='developer',
        #     y='project'
        # )
        #
        # c = alt.Chart(df[['project', 'developer', 'task date']]).mark_bar().encode(
        #     x='developer', y='project', size='task date', color='task date',
        #     tooltip=['project', 'developer', 'task date'])
        #
        # st.altair_chart(c, use_container_width=True)
        #
        # st.title('Altair plot')
        # st.altair_chart(chart, use_container_width=True)
        #
        # st.title('Streamlit plot')
        # st.bar_chart(df[['project', 'developer']])
        #
        # # daily_cases = df.groupby(pd.Grouper(key="date", freq="1D"))
        # # fig = daily_cases.plot(kind="line", asFigure=True,
        # #                         x="date", y="developer")
        # # st.plotly_chart(fig)

        pr = df.profile_report()
        st_profile_report(pr)
