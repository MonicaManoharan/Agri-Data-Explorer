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
    st.markdown("<h1 style='text-align: center;'>📊 Policymaker Dashboard</h1>", unsafe_allow_html=True)
    selected_tab = st.sidebar.radio("📊 Policymaker Dashboard Sections", 
                                    ["Production Insights", "Recommendations"])
    if selected_tab == "Production Insights":
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
    
    elif selected_tab == "Recommendations":
        # st.markdown("<h2 style='text-align: center;'>Crop Recommendations for Profit</h2>", unsafe_allow_html=True)
        st.subheader("Recommendations for Policymakers")

        with st.expander("📈 Key Crop Insights"):
            st.markdown("✅ Based on the production trends across states and years, here are some strategic insights:")

            # 1. High-yield crop recommendation
            top_crop_total = df[[
                "rice_production_1000_tons",
                "wheat_production_1000_tons",
                "sugarcane_production_1000_tons",
                "pearl_millet_production_1000_tons"
            ]].sum().sort_values(ascending=False)
            
            top_crop = top_crop_total.idxmax().replace("_production_1000_tons", "").title()
            st.markdown(f"🌾 **{top_crop}** is currently the most produced crop nationwide. Consider increasing investment in its supply chain, storage, and exports.")

            # 3. Fastest growing crop (YOY growth)
            yearly_trend = df.groupby("year")[["rice_production_1000_tons", "wheat_production_1000_tons", "sugarcane_production_1000_tons"]].sum()
            growth = yearly_trend.pct_change().mean().sort_values(ascending=False)
            fastest_crop = growth.idxmax().replace("_production_1000_tons", "").title()
            st.markdown(f"🚀 **{fastest_crop}** is the fastest-growing crop in recent years. Encourage research and development for better yield and value-added products.")

        with st.expander("📊 State-Level Recommendations"):
            top_states = df.groupby("state_name")[["rice_production_1000_tons", "wheat_production_1000_tons"]].sum()
            best_rice_state = top_states["rice_production_1000_tons"].idxmax()
            best_wheat_state = top_states["wheat_production_1000_tons"].idxmax()

            st.markdown(f"🏅 **{best_rice_state}** leads in rice production – focus on maintaining water-efficient practices.")
            st.markdown(f"🥇 **{best_wheat_state}** leads in wheat – invest in sustainable storage and wheat-based industries.")

        with st.expander("🌿 Sustainability Suggestions"):
            st.markdown("""
            - 💧 Promote **drip irrigation** in water-scarce districts.
            - 🌾 Encourage **millet cultivation** in dryland areas to diversify risk.
            - 📦 Improve **cold storage** and **transport logistics** to reduce post-harvest losses.
            - 🛰️ Use **remote sensing & AI** to monitor soil health and recommend optimal crops.
            """)

    
