
import streamlit as st

def calculate_dredging_unit_rate(params):
    production_rate = params.get('production_rate', 2000)
    total_volume = params.get('total_volume', 2000000)
    fuel_consumption = params.get('fuel_consumption', 500)
    fuel_price = params.get('fuel_price', 2)
    labor_cost = params.get('labor_cost', 500)
    maintenance_percent = params.get('maintenance_percent', 0.003)
    new_build_value = params.get('new_build_value', 10000000)
    disposal_cost = params.get('disposal_cost', 0.2)
    overhead_markup = params.get('overhead_markup', 0.05)
    mobilization_cost = params.get('mobilization_cost', 500000)
    demobilization_cost = params.get('demobilization_cost', 500000)
    workboat_daily_rate = params.get('workboat_daily_rate', 10000)
    workboat_rental_days = params.get('workboat_rental_days', 100)
    pipeline_cost_per_meter = params.get('pipeline_cost_per_meter', 600)
    pipeline_length = params.get('pipeline_length', 2000)
    depreciation_period = params.get('depreciation_period', 20)
    financing_rate = params.get('financing_rate', 0.07)
    project_days = params.get('project_days', 125)

    hours_required = total_volume / production_rate
    fuel_cost_total = hours_required * fuel_consumption * fuel_price
    labor_cost_total = hours_required * labor_cost
    maintenance_cost_total = new_build_value * maintenance_percent
    disposal_cost_total = total_volume * disposal_cost
    workboat_cost = workboat_daily_rate * workboat_rental_days
    pipeline_total_cost = pipeline_cost_per_meter * pipeline_length
    depreciation_allocation = (new_build_value / depreciation_period) * (project_days / 365)
    financing_allocation = (new_build_value * financing_rate) * (project_days / 365)

    direct_costs = fuel_cost_total + labor_cost_total + maintenance_cost_total + disposal_cost_total + mobilization_cost + demobilization_cost + workboat_cost + pipeline_total_cost + depreciation_allocation + financing_allocation
    overhead_cost = direct_costs * overhead_markup
    total_cost = direct_costs + overhead_cost
    unit_rate = total_cost / total_volume

    return {'total_cost': total_cost, 'unit_rate': unit_rate}

st.title('Dredging Unit Rate Calculator')

dredger_type = st.selectbox('Dredger Type', ['CSD', 'TSHD'])
production_rate = st.number_input('Production Rate (m³/hr)', value=2000)
fuel_consumption = st.number_input('Fuel Consumption (l/hr)', value=500)
fuel_price = st.number_input('Fuel Price (€ per liter)', value=2.0)
labor_cost = st.number_input('Labor Cost (€/hr)', value=500)
maintenance_percent = st.number_input('Maintenance Percentage (%)', value=0.3) / 100
new_build_value = st.number_input('New Build Value (€)', value=10000000)
disposal_cost = st.number_input('Disposal Cost (€/m³)', value=0.2)
overhead_markup = st.number_input('Overhead Markup (%)', value=5) / 100
mobilization_cost = st.number_input('Mobilization Cost (€)', value=500000)
demobilization_cost = st.number_input('Demobilization Cost (€)', value=500000)
workboat_rental_days = st.number_input('Workboat Rental Days', value=100)
workboat_daily_rate = st.number_input('Workboat Daily Rate (€)', value=10000)
pipeline_length = st.number_input('Pipeline Length (m)', value=2000)
pipeline_cost_per_meter = st.number_input('Pipeline Cost per Meter (€)', value=600)
depreciation_period = st.number_input('Depreciation Period (years)', value=20)
financing_rate = st.number_input('Financing Rate (%)', value=7) / 100

if st.button('Calculate Unit Rate'):
    params = {
        'production_rate': production_rate,
        'total_volume': 2000000,
        'fuel_consumption': fuel_consumption,
        'fuel_price': fuel_price,
        'labor_cost': labor_cost,
        'maintenance_percent': maintenance_percent,
        'new_build_value': new_build_value,
        'disposal_cost': disposal_cost,
        'overhead_markup': overhead_markup,
        'mobilization_cost': mobilization_cost,
        'demobilization_cost': demobilization_cost,
        'workboat_rental_days': workboat_rental_days,
        'workboat_daily_rate': workboat_daily_rate,
        'pipeline_length': pipeline_length,
        'pipeline_cost_per_meter': pipeline_cost_per_meter,
        'depreciation_period': depreciation_period,
        'financing_rate': financing_rate,
        'project_days': 125
    }
    result = calculate_dredging_unit_rate(params)
    st.success(f"Total Project Cost: €{result['total_cost']:,.2f}")
    st.info(f"Unit Rate: €{result['unit_rate']:.2f} per m³")
