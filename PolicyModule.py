import streamlit as st
import plotly.express as px

def policymaker_dashboard(df):
    
    st.set_page_config(layout="wide", page_title="Policymaker Dashboard", page_icon="📊")

    # Remove padding
    st.markdown("""
        <style>
            .block-container {
                padding: 1rem 0rem;
            }
        </style>
    """, unsafe_allow_html=True)

    # st.image("assets/researcher_section_bg.png", use_container_width=True)
    st.markdown("<h1 style='text-align: center;'>Policymaker Dashboard</h1>", unsafe_allow_html=True)

    # st.header("Policymaker Dashboard")

    # === Row 1 ===
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Sugarcane Production Trend")
        sugarcane_data = df.groupby("year")["sugarcane_production_1000_tons"].sum()
        fig = px.line(
            sugarcane_data,
            x=sugarcane_data.index,
            y=sugarcane_data.values,
            labels={'x': 'Year', 'y': 'Sugarcane Production'},
            markers=True,
            color_discrete_sequence=['brown']
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Rice vs Wheat Production (Last 50 Years)")
        fig = px.line()
        for crop in ["rice_production_1000_tons", "wheat_production_1000_tons"]:
            crop_data = df.groupby("year")[crop].sum()
            fig.add_scatter(
                x=crop_data.index,
                y=crop_data.values,
                mode='lines+markers',
                name=crop.replace("_production_1000_tons", "").title()
            )
        st.plotly_chart(fig, use_container_width=True)

    # === Row 2 ===
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Rice Production by West Bengal Districts")
        wb_data = df[df["state_name"] == "West Bengal"].groupby("dist_name")["rice_production_1000_tons"].sum()
        fig = px.bar(
            wb_data,
            x=wb_data.index,
            y=wb_data.values,
            labels={'x': 'District', 'y': 'Rice Production'},
            color=wb_data.values,
            color_continuous_scale='greens'
        )
        fig.update_layout(
            coloraxis_colorbar=dict(title="Production Level")  # Custom title
        )
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        st.subheader("Top 10 Wheat Production Years in Uttar Pradesh")
        up_data = df[df["state_name"] == "Uttar Pradesh"].groupby("year")["wheat_production_1000_tons"].sum().nlargest(10)
        fig = px.bar(
            up_data,
            x=up_data.index,
            y=up_data.values,
            labels={'x': 'Year', 'y': 'Wheat Production'},
            color=up_data.values,
            color_continuous_scale='blues'
        )
        fig.update_layout(
            coloraxis_colorbar=dict(title="Production Level")  # Custom title
        )
        st.plotly_chart(fig, use_container_width=True)

    # === Row 3 ===
    st.subheader("Millet Production Trend")
    millet_data = df.groupby("year")["pearl_millet_production_1000_tons"].sum()
    fig = px.line(
        millet_data,
        x=millet_data.index,
        y=millet_data.values,
        labels={'x': 'Year', 'y': 'Millet Production'},
        markers=True,
        color_discrete_sequence=['purple']
    )
    st.plotly_chart(fig, use_container_width=True)
