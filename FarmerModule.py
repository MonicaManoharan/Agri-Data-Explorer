# import streamlit as st
# import plotly.express as px

# def farmer_dashboard(df):
#     st.image("assets/farmer_section_bg.png", use_container_width=True)
#     st.header("Farmer Dashboard")

#     # Top 7 Rice Producing States (Bar Plot)
#     st.subheader("Top 7 Rice Producing States")
#     rice_data = df.groupby("state_name")["rice_production_1000_tons"].sum().nlargest(7)
#     fig = px.bar(rice_data, x=rice_data.index, y=rice_data.values, 
#                  labels={'x': 'State', 'y': 'Rice Production (1000 tons)'},
#                  color=rice_data.values, color_continuous_scale='greens')
#     st.plotly_chart(fig, use_container_width=True)

#     # Top 5 Wheat Producing States (Pie Chart)
#     st.subheader("Top 5 Wheat Producing States")
#     wheat_data = df.groupby("state_name")["wheat_production_1000_tons"].sum().nlargest(5)
#     fig = px.pie(values=wheat_data.values, names=wheat_data.index, title="Wheat Production Percentage")
#     st.plotly_chart(fig, use_container_width=True)

#     # Oilseed Production by Top 5 States (Bar Plot)
#     st.subheader("Oilseed Production by Top 5 States")
#     oilseed_data = df.groupby("state_name")["oilseeds_production_1000_tons"].sum().nlargest(5)
#     fig = px.bar(oilseed_data, x=oilseed_data.index, y=oilseed_data.values, 
#                  labels={'x': 'State', 'y': 'Oilseed Production (1000 tons)'},
#                  color=oilseed_data.values, color_continuous_scale='oranges')
#     st.plotly_chart(fig, use_container_width=True)

#     # Top 7 Sunflower Producing States (Bar Plot)
#     st.subheader("Top 7 Sunflower Producing States")
#     sunflower_data = df.groupby("state_name")["sunflower_production_1000_tons"].sum().nlargest(7)
#     fig = px.bar(
#             sunflower_data,
#             x=sunflower_data.index,
#             y=sunflower_data.values,
#             labels={'x': 'State', 'y': 'Sunflower Production (1000 tons)'},
#             color=sunflower_data.values,
#             color_continuous_scale='ylorrd'  # Valid Plotly colorscale
#         )
#     st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import plotly.express as px

def farmer_dashboard(df):
 
    st.set_page_config(layout="wide", page_title="Farmer Dashboard", page_icon="🌱")

    # Remove padding
    st.markdown("""
        <style>
            .block-container {
                padding: 1rem 0rem;
            }
        </style>
    """, unsafe_allow_html=True)

    # st.image("assets/researcher_section_bg.png", use_container_width=True)
    st.markdown("<h1 style='text-align: center;'>Farmer Dashboard</h1>", unsafe_allow_html=True)

    # st.image("assets/farmer_section_bg.png", use_container_width=True)
    # st.header("Farmer Dashboard")

    # Create first row with two columns
    col1, col2 = st.columns(2)

    with col1:
        # Top 7 Rice Producing States (Bar Plot)
        st.subheader("Top 7 Rice Producing States")
        rice_data = df.groupby("state_name")["rice_production_1000_tons"].sum().nlargest(7)
        fig = px.bar(
            rice_data,
            x=rice_data.index,
            y=rice_data.values,
            labels={'x': 'State', 'y': 'Rice Production (1000 tons)'},
            color=rice_data.values,
            color_continuous_scale='greens'
        )
        fig.update_layout(
            coloraxis_colorbar=dict(title="Production Level")  # Custom title
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Top 5 Wheat Producing States (Pie Chart)
        st.subheader("Top 5 Wheat Producing States")
        wheat_data = df.groupby("state_name")["wheat_production_1000_tons"].sum().nlargest(5)
        fig = px.pie(
            values=wheat_data.values,
            names=wheat_data.index,
            title="Wheat Production Percentage"
        )
        st.plotly_chart(fig, use_container_width=True)

    # Create second row with two columns
    col3, col4 = st.columns(2)

    with col3:
        # Oilseed Production by Top 5 States (Bar Plot)
        st.subheader("Oilseed Production by Top 5 States")
        oilseed_data = df.groupby("state_name")["oilseeds_production_1000_tons"].sum().nlargest(5)
        fig = px.bar(
            oilseed_data,
            x=oilseed_data.index,
            y=oilseed_data.values,
            labels={'x': 'State', 'y': 'Oilseed Production (1000 tons)'},
            color=oilseed_data.values,
            color_continuous_scale='oranges'
        )
        fig.update_layout(
            coloraxis_colorbar=dict(title="Production Level")  # Custom title
        )
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        # Top 7 Sunflower Producing States (Bar Plot)
        st.subheader("Top 7 Sunflower Producing States")
        sunflower_data = df.groupby("state_name")["sunflower_production_1000_tons"].sum().nlargest(7)
        fig = px.bar(
            sunflower_data,
            x=sunflower_data.index,
            y=sunflower_data.values,
            labels={'x': 'State', 'y': 'Sunflower Production (1000 tons)'},
            color=sunflower_data.values,
            color_continuous_scale='blues'
        )
        fig.update_layout(
            coloraxis_colorbar=dict(title="Production Level")  # Custom title
        )
        st.plotly_chart(fig, use_container_width=True)
