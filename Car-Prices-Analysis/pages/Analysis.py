# import needed libraries
import streamlit as st
import EDA
from EDA import df_cleaned as df

tab_top_cars_models, tab_total_sales, tab_prices, tab_sellers, tab_states = st.tabs(
    ['Top Cars Analysis', 'Total Sales Analysis', 'Price Analysis', 'Seller Analysis', 'States Analysis'])

with tab_top_cars_models:
    # Title of tab
    st.title('Top Cars Brand and Models Analysis')

    # insights in this tab
    st.write('The information in this tab can answer the following questions :')
    st.write('    1- What are the most common car brands and models ?')
    st.write('    2- What are the most common body types ?')
    st.write('    3- What is the distribution of colors (exterior/interior) among the listed vehicles?')

    # First section
    st.header('1- What are the most common car brands and models ?')
    st.write('Ford, Chevrolet and Nissan are on top of the market')
    st.write('Most sold models are kinda close in sales')
    cont = st.container()
    cont1, cont2 = cont.columns(2)
    with cont1:
        dim = st.radio(
            "Select fact of your interest",
            ["brand", "model"],
            key="Tab 1, top car dimension",
            horizontal=True,
        )
    with cont2:
        n = st.radio(
            "Select number to show",
            [5, 15, 25, 50],
            key="Tab 1, top car number",
            horizontal=True,
        )
    st.plotly_chart(EDA.top(df, dim, n))

    # Second section
    st.header('2- What are the most common body types ?')
    st.write('Sedan and SUV are the most common')
    num = st.radio(
        "Select number to show",
        [5, 10, 25],
        key='Tab 1 Body types',
        horizontal=True,
    )
    st.plotly_chart(EDA.top_body_type(df, num))

    # Third section
    st.header('3- What is the distribution of colors (exterior/interior) among the listed vehicles ?')
    st.write("Black is people's favourite color")
    cont = st.container()
    cont1, cont2 = cont.columns(2)
    with cont1:
        dim = st.radio(
            "Select fact of your interest",
            ["color", "interior"],
            key="Tab 1, top car color",
            horizontal=True,
        )
    with cont2:
        n = st.radio(
            "Select number to show",
            [5, 15, 25],
            key="Tab 1, top car color n",
            horizontal=True,
        )
    st.plotly_chart(EDA.top_colors(df, dim, n))

with tab_total_sales:
    # Title of tab
    st.title("Total Sales Analysis By Car & Time")

    # insights in this tab
    st.write('The information in this tab can answer the following questions :')
    st.write('    1. What is the total sales generated by the listed vehicles?')
    st.write('    2. Do people tend to buy more in a certain day')
    st.write('    3. Do people tend to buy more in a certain month')

    # First section
    st.header('1. What is the total sales generated by the listed vehicles?')
    st.write('It confirms the most sold cars in Top Cars Analysis')
    cont = st.container()
    cont1, cont2 = cont.columns(2)
    with cont1:
        dim = st.radio(
            "Select fact of your interest",
            ["brand", "model"],
            key="Tab 2 dimensional_selection total sales",
            horizontal=True,
        )
    with cont2:
        n = st.radio(
            "Select number to show",
            [5, 15, 25, 50],
            key="Tab 2 number selection total sales",
            horizontal=True,
        )
    st.plotly_chart(EDA.total_sales_by_type(df, dim, n))

    # Second section
    st.header('2. Do people tend to buy more in a certain day/month')
    st.write('People prefer certain days')
    st.plotly_chart(EDA.sales_by_day(df))

    # Third section
    st.header('3. Do people tend to buy more in a certain month')
    st.write('People also prefer certain months')
    st.plotly_chart(EDA.sales_by_month(df))

with tab_prices:
    # Title of tab
    st.title('Price Analysis by Vehicle Attributes')

    # insights in this tab
    st.write('The information in this tab can answer the following questions :')
    st.write('    1. What is the average selling price for each car brand and model ?')
    st.write('    2. Is there a correlation between odometer readings and selling prices ?')
    st.write('    3. Is there a correlation between car condition and selling price ?')
    st.write('    4. Does car color (exterior/interior) contribute to price ?')

    # First section
    st.header('1. What is the average selling price for each car brand and model ?')
    st.write('Rolls Royce is the most expensive brand, but the most expensive model is from Ferrari')
    cont = st.container()
    cont1, cont2 = cont.columns(2)
    with cont1:
        dim = st.radio(
            "Select fact of your interest",
            ["brand", "model"],
            key='Tab 3 car avg price',
            horizontal=True,
        )
    with cont2:
        n = st.radio(
            "Select number to show",
            [5, 15, 25, 50],
            key='Tab 3 car avg price number',
            horizontal=True,
        )
    st.plotly_chart(EDA.avg_price(df, dim, n))

    # Second section
    st.header('2. Is there a correlation between odometer readings and selling prices ?')
    st.write('The higher the milage, the lower the price')
    st.plotly_chart(EDA.odo_sell(df))

    # Third section
    st.header('3. Is there a correlation between car condition and selling price ?')
    st.write('The better the condition, the higher the price')
    st.plotly_chart(EDA.cond_sell(df))

    # Fourth section
    st.header('4. Does car color (exterior/interior) contribute to price ?')
    cont = st.container()
    cont1, cont2 = cont.columns(2)
    with cont1:
        dim = st.radio(
            "Select fact of your interest",
            ["color", "interior"],
            key='Tab 3 car color price',
            horizontal=True,
        )
    with cont2:
        n = st.radio(
            "Select number to show",
            [5, 15, 25],
            key='Tab 3 car color price number',
            horizontal=True,
        )
    st.plotly_chart(EDA.col_int_sell(df, dim, n))

with tab_sellers:
    # Title of tab
    st.title('Seller Performance Analysis')

    # insights in this tab
    st.write('The information in this tab can answer the following questions :')
    st.write('    1. What is the total number of vehicles sold by each seller ?')
    st.write('    2. What is the total sales revenue generated by each seller ?')
    st.write('    3. What is the average odometer reading of car for each seller ?')

    # First section
    st.header('1. What is the total number of vehicles sold by each seller ?')
    n = st.radio(
        "Select number to show",
        [5, 10, 25],
        key='Tab 4 total cars sold seller n',
        horizontal=True,
    )
    st.plotly_chart(EDA.top_sellers_count(n))

    # Second section
    st.header('2. What is the total sales revenue generated by each seller ?')
    n = st.radio(
        "Select number to show",
        [5, 10, 25],
        key='Tab 4 total sales seller n',
        horizontal=True,
    )
    st.plotly_chart(EDA.top_sellers_sales(n))

    # Third section
    st.header('3. What is the average odometer reading of car for each seller ?')
    n = st.radio(
        "Select number to show",
        [5, 10, 25],
        key='Tab 4 avg odometer seller n',
        horizontal=True,
    )
    st.plotly_chart(EDA.avg_odometer_seller(n))


with tab_states:
    # Title of tab
    st.title('State-wise Analysis')

    # insights in this tab
    st.write('The information in this tab can answer the following questions :')
    st.write('    1. What are the top states with the highest total sales revenue ?')
    st.write('    2. What is the distribution of vehicle conditions in each state ?')
    st.write('    3. What is the average selling price of vehicles in each state ?')

    # First section
    st.header('1. What are the top states with the highest total sales revenue ?')
    n = st.radio(
        "Select number to show",
        [5, 10, 25],
        key='Tab 5 highest sales states n',
        horizontal=True,
    )
    st.plotly_chart(EDA.sales_per_state(n))

    # Second section
    st.header('2. What is the distribution of vehicle conditions in each state ?')
    n = st.radio(
        "Select number to show",
        [5, 10, 25],
        key='Tab 5 condition in each state n',
        horizontal=True,
    )
    st.plotly_chart(EDA.condition_state(n))

    # Third section
    st.header('3. What is the average selling price of vehicles in each state ?')
    n = st.radio(
        "Select number to show",
        [5, 10, 25],
        key='Tab 5 avg selling price per state n',
        horizontal=True,
    )
    st.plotly_chart(EDA.avg_price_state(n))