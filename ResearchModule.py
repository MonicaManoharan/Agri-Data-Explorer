import streamlit as st
import plotly.express as px

def researcher_dashboard(df):
    # Wide layout
    st.set_page_config(layout="wide", page_title="Researcher Dashboard", page_icon="🧪")

    # Remove padding
    st.markdown("""
        <style>
            .block-container {
                padding: 1rem 0rem;
            }
        </style>
    """, unsafe_allow_html=True)


    st.markdown("<h1 style='text-align: center;'>Researcher Dashboard</h1>", unsafe_allow_html=True)
    selected_tab = st.sidebar.radio("🧪Researcher Dashboard Sections", 
                                    ["Production Insights", "Recommendations"])
    
    if selected_tab == "Production Insights":
        # === Row 1 ===
        col1, col2 = st.columns([6, 6])
        with col1:
            st.subheader("Sorghum Production (Kharif and Rabi) by Region")
            sorghum_data = df.groupby("state_name")[[
                "kharif_sorghum_production_1000_tons", "rabi_sorghum_production_1000_tons"]].sum().reset_index()
            fig1 = px.bar(sorghum_data, x="state_name", 
                        y=["kharif_sorghum_production_1000_tons", "rabi_sorghum_production_1000_tons"],
                        labels={'value': 'Production (1000 tons)', 'state_name': 'State'}, barmode='stack')
            fig1.update_layout(
                coloraxis_colorbar=dict(title="Production Level")  # Custom title
            )
            st.plotly_chart(fig1, use_container_width=True)

        with col2:
            st.subheader("Top 7 States for Groundnut Production")
            groundnut_data = df.groupby("state_name")["groundnut_production_1000_tons"].sum().nlargest(7)
            fig2 = px.bar(
                groundnut_data,
                x=groundnut_data.index,
                y=groundnut_data.values,
                labels={'x': 'State', 'y': 'Groundnut Production'},
                color=groundnut_data.values,
                color_continuous_scale='oranges'
            )
            fig2.update_layout(
                coloraxis_colorbar=dict(title="Production Level")  # Custom title
            )
            st.plotly_chart(fig2, use_container_width=True)

        # === Row 2 ===
        col3, col4 = st.columns([6, 6])
        with col3:
            st.subheader("Soybean Production and Yield Efficiency")
            soy_data = df.groupby("state_name")[["soyabean_production_1000_tons", "soyabean_yield_kg_per_ha"]].sum().nlargest(5, "soyabean_production_1000_tons")
            fig3 = px.bar(soy_data, x=soy_data.index, y="soyabean_production_1000_tons",
                        labels={'x': 'State', 'y': 'Soybean Production'},
                        color="soyabean_production_1000_tons", color_continuous_scale='purples')
            fig3.update_layout(
                coloraxis_colorbar=dict(title="Production Level")  # Custom title
            )
            st.plotly_chart(fig3, use_container_width=True)

        with col4:
            st.subheader("Oilseed Production in Major States")
            oilseed_data = df.groupby("state_name")["oilseeds_production_1000_tons"].sum()
            fig4 = px.bar(oilseed_data, x=oilseed_data.index, y=oilseed_data.values,
                        labels={'x': 'State', 'y': 'Oilseed Production'},
                        color=oilseed_data.values, color_continuous_scale='oranges')
            fig4.update_layout(
                coloraxis_colorbar=dict(title="Production Level")  # Custom title
            )
            st.plotly_chart(fig4, use_container_width=True)

        # === Row 3 ===
        col5, col6 = st.columns([6, 6])
        with col5:
            st.subheader("Impact of Area Cultivated on Production")
            fig5 = px.scatter(df, x="rice_area_1000_ha", y="rice_production_1000_tons",
                            labels={'x': 'Rice Area (1000 ha)', 'y': 'Rice Production (1000 tons)'},
                            color_discrete_sequence=['green'])
            st.plotly_chart(fig5, use_container_width=True)

        with col6:
            st.subheader("Rice vs Wheat Yield Across States")
            yield_data = df.groupby("state_name")[["rice_yield_kg_per_ha", "wheat_yield_kg_per_ha"]].mean().reset_index()
            fig6 = px.bar(yield_data, x="state_name", 
                        y=["rice_yield_kg_per_ha", "wheat_yield_kg_per_ha"],
                        labels={'value': 'Yield (Kg per ha)', 'state_name': 'State'},
                        barmode='group')
            fig6.update_layout(
                coloraxis_colorbar=dict(title="Production Level")  # Custom title
            )
            st.plotly_chart(fig6, use_container_width=True)

    elif selected_tab == "Recommendations":
        st.markdown("<h2 style='text-align: center;'>Researcher Recommendations</h2>", unsafe_allow_html=True)

        # Layout: Left spacer, center content, right spacer
        left, center, right = st.columns([1, 2, 1])

        with center:
            st.markdown("""
                    🔬 **Sorghum Insights**  
                    ▪️ 📈 High production seen in states like Maharashtra and Karnataka.  
                    ▪️ 🌾 Research on drought-resistant Kharif/Rabi sorghum varieties is encouraged.  

                    🥜 **Groundnut Trends**  
                    ▪️ 🏆 Gujarat and Andhra Pradesh lead in groundnut production.  
                    ▪️ 🧪 Focus on disease-resistant groundnut breeds can improve yield.

                    🌱 **Soybean Production**  
                    ▪️ 💪 Madhya Pradesh and Maharashtra dominate soybean yield.  
                    ▪️ 📊 Correlate soil quality and rainfall data to optimize yield efficiency.

                    🌻 **Oilseed Cultivation**  
                    ▪️ 🌿 Increasing trends suggest potential for biofuel research.  
                    ▪️ 🛠️ Recommend innovation in post-harvest oil extraction methods.
                    """)
