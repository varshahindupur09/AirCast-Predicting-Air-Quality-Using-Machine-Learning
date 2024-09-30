import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import requests
import random
import requests
import streamlit as st
import pandas as pd
import json
import openai
from streamlit_extras.switch_page_button import switch_page
from dotenv import load_dotenv
import re
import random
import os
load_dotenv()
def check_four_digit_number(string):
    # Compile the regular expression
    regex = re.compile(r'^\d{4,5}$')
    # Check if the string matches the pattern
    if regex.search(string):
        return True
    else:
        return False
def generate_openai_result(pollulant_value):
    aqi = random.randint(36, 40)

    parameter = "ozone"
    #setting the API KEY here
    openai.api_key = os.environ.get('OPEN_AI_API_KEY')
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages = [
        {'role': 'user', 'content': "I am an air quality expert. Answer the below in less than 50 words as an air quality expert: what are effects of AQI {} {} what range is it in and what are the effects on health?".format(aqi, parameter)}
    ],
    temperature = 0.10)

    response  = completion.choices[0].message.content
    return response

if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = False
if 'user_status' not in st.session_state:
    st.session_state['user_status'] = 2    ## 1 for Admin and 2 for User
if 'forgot_status' not in st.session_state:
    st.session_state['forgot_status'] = False
if 'reg_status' not in st.session_state:
    st.session_state['reg_status'] = False
if st.session_state['authentication_status'] ==  False:
    st.markdown("#### Please Use the Login Screen")
else:
    st.title('Air Cast-  Reliable air quality prediction in your area')
    zip_input = st.text_input('Enter Your ZipCode please')
    search_btn = st.button('Search', key = 'Search')

    if search_btn:
            my_list = ['1001',
            '1002',
            '1005',
            '1007',
            '1008',
            '1010',
            '1011',
            '1012',
            '1013',
            '1020',
            '1022',
            '1026',
            '1027',
            '1028',
            '1029',
            '1030',
            '1031',
            '1032',
            '1033',
            '1034',
            '1035',
            '1036',
            '1037',
            '1038',
            '1039',
            '1040',
            '1050',
            '1053',
            '1054',
            '1056',
            '1057',
            '1060',
            '1062',
            '1068',
            '1069',
            '1070',
            '1071',
            '1072',
            '1073',
            '1075',
            '1077',
            '1080',
            '1081',
            '1082',
            '1083',
            '1084',
            '1085',
            '1088',
            '1089',
            '1092',
            '1095',
            '1096',
            '1098',
            '1103',
            '1104',
            '1105',
            '1106',
            '1107',
            '1108',
            '1109',
            '1118',
            '1119',
            '1128',
            '1129',
            '1151',
            '1201',
            '1220',
            '1222',
            '1223',
            '1225',
            '1226',
            '1230',
            '1235',
            '1236',
            '1237',
            '1238',
            '1240',
            '1242',
            '1244',
            '1245',
            '1247',
            '1253',
            '1254',
            '1255',
            '1256',
            '1257',
            '1258',
            '1259',
            '1262',
            '1264',
            '1266',
            '1267',
            '1301',
            '1330',
            '1331',
            '1337',
            '1338',
            '1339',
            '1340',
            '1341',
            '1342',
            '1344',
            '1346',
            '1349',
            '1350',
            '1351',
            '1355',
            '1360',
            '1364',
            '1366',
            '1367',
            '1368',
            '1370',
            '1373',
            '1375',
            '1376',
            '1378',
            '1379',
            '1420',
            '1430',
            '1431',
            '1432',
            '1436',
            '1438',
            '1440',
            '1450',
            '1451',
            '1452',
            '1453',
            '1460',
            '1462',
            '1463',
            '1464',
            '1467',
            '1468',
            '1469',
            '1473',
            '1474',
            '1475',
            '1501',
            '1503',
            '1504',
            '1505',
            '1506',
            '1507',
            '1510',
            '1515',
            '1516',
            '1518',
            '1519',
            '1520',
            '1521',
            '1522',
            '1523',
            '1524',
            '1527',
            '1529',
            '1531',
            '1532',
            '1534',
            '1535',
            '1536',
            '1537',
            '1540',
            '1541',
            '1542',
            '1543',
            '1545',
            '1550',
            '1560',
            '1562',
            '1564',
            '1566',
            '1568',
            '1569',
            '1570',
            '1571',
            '1581',
            '1583',
            '1585',
            '1588',
            '1590',
            '1602',
            '1603',
            '1604',
            '1605',
            '1606',
            '1607',
            '1608',
            '1609',
            '1610',
            '1611',
            '1612',
            '1701',
            '1702',
            '1718',
            '1719',
            '1720',
            '1721',
            '1730',
            '1731',
            '1740',
            '1741',
            '1742',
            '1745',
            '1746',
            '1747',
            '1748',
            '1749',
            '1752',
            '1754',
            '1756',
            '1757',
            '1760',
            '1770',
            '1772',
            '1773',
            '1775',
            '1776',
            '1778',
            '1801',
            '1803',
            '1810',
            '1821',
            '1824',
            '1826',
            '1827',
            '1830',
            '1832',
            '1833',
            '1834',
            '1835',
            '1840',
            '1841',
            '1843',
            '1844',
            '1845',
            '1850',
            '1851',
            '1852',
            '1854',
            '1860',
            '1862',
            '1863',
            '1864',
            '1867',
            '1876',
            '1879',
            '1880',
            '1886',
            '1887',
            '1890',
            '1902',
            '1904',
            '1905',
            '1906',
            '1907',
            '1908',
            '1913',
            '1915',
            '1921',
            '1922',
            '1923',
            '1929',
            '1930',
            '1938',
            '1940',
            '1944',
            '1945',
            '1949',
            '1950',
            '1951',
            '1952',
            '1960',
            '1966',
            '1969',
            '1970',
            '1982',
            '1983',
            '1984',
            '1985',
            '2019',
            '2021',
            '2025',
            '2026',
            '2030',
            '2032',
            '2035',
            '2038',
            '2043',
            '2045',
            '2048',
            '2050',
            '2052',
            '2053',
            '2054',
            '2056',
            '2061',
            '2062',
            '2066',
            '2067',
            '2071',
            '2072',
            '2081',
            '2090',
            '2093',
            '2108',
            '2109',
            '2110',
            '2111',
            '2113',
            '2114',
            '2115',
            '2116',
            '2118',
            '2119',
            '2120',
            '2121',
            '2122',
            '2124',
            '2125',
            '2126',
            '2127',
            '2128',
            '2129',
            '2130',
            '2131',
            '2132',
            '2134',
            '2135',
            '2136',
            '2138',
            '2139',
            '2140',
            '2141',
            '2142',
            '2143',
            '2144',
            '2145',
            '2148',
            '2149',
            '2150',
            '2151',
            '2152',
            '2155',
            '2163',
            '2169',
            '2170',
            '2171',
            '2176',
            '2180',
            '2184',
            '2186',
            '2188',
            '2189',
            '2190',
            '2191',
            '2199',
            '2210',
            '2215',
            '2301',
            '2302',
            '2322',
            '2324',
            '2330',
            '2332',
            '2333',
            '2338',
            '2339',
            '2341',
            '2343',
            '2346',
            '2347',
            '2351',
            '2356',
            '2359',
            '2360',
            '2364',
            '2366',
            '2367',
            '2368',
            '2370',
            '2375',
            '2379',
            '2382',
            '2420',
            '2421',
            '2445',
            '2446',
            '2451',
            '2452',
            '2453',
            '2458',
            '2459',
            '2460',
            '2461',
            '2462',
            '2464',
            '2465',
            '2466',
            '2467',
            '2468',
            '2472',
            '2474',
            '2476',
            '2478',
            '2481',
            '2482',
            '2492',
            '2493',
            '2494',
            '2532',
            '2534',
            '2535',
            '2536',
            '2537',
            '2538',
            '2539',
            '2540',
            '2542',
            '2543',
            '2554',
            '2556',
            '2558',
            '2559',
            '2563',
            '2568',
            '2571',
            '2575',
            '2576',
            '2601',
            '2630',
            '2631',
            '2632',
            '2633',
            '2635',
            '2638',
            '2639',
            '2642',
            '2644',
            '2645',
            '2646',
            '2647',
            '2648',
            '2649',
            '2650',
            '2652',
            '2653',
            '2655',
            '2657',
            '2659',
            '2660',
            '2664',
            '2666',
            '2667',
            '2668',
            '2669',
            '2670',
            '2671',
            '2672',
            '2673',
            '2675',
            '2702',
            '2703',
            '2713',
            '2715',
            '2717',
            '2718',
            '2719',
            '2720',
            '2721',
            '2723',
            '2724',
            '2725',
            '2726',
            '2738',
            '2739',
            '2740',
            '2743',
            '2744',
            '2745',
            '2746',
            '2747',
            '2748',
            '2760',
            '2762',
            '2763',
            '2764',
            '2766',
            '2767',
            '2769',
            '2770',
            '2771',
            '2777',
            '2779',
            '2780',
            '2790']
            zip_ma = [f"0{x}" if len(x) == 4 else x for x in my_list] 
            if not check_four_digit_number(zip_input):
                st.error("Input not ZipCode valid")
            else:
                if zip_input not in zip_ma:
                    st.error("Sorry we currently provide servie to MA state only")
                else:
                    token = st.session_state["authentication_status"]
                    headers = {'Authorization': f'Bearer {token}'}
                    # user_id = df_result_user_list.loc[df_result_user_list['username'] == st.session_state['user'], 'id'].item()
                        # print(user)
                        # print(user_id)
                    # date_request = date_selected.strftime("%m/%d/%Y")
                        # print(date_request)
                    # payload = {'date_request':date_request}

                    result = requests.get(f"http://backend:8000/aircast/prediction-for-zipcode?zipcode={zip_input}",headers=headers)
            
                    if result.status_code == 200:
                        st.subheader(":blue[AQI Insights]")
                        # Set the AQI value and parameter
                        print(result.status_code, "Status code")
                        
                        insight = generate_openai_result('insight')
                        st.write(insight)
                        output = result.json()
                        print(output)
                        db_elements = list(output['stations'][0].keys())
                        predictions = pd.DataFrame(output['stations'])
                        print(type(predictions))
                        print(predictions)
                        print("********* db_elements**********")
                        print(db_elements)
                        for el in db_elements:
                            if el == "OZONE":
                                # print(el)
                                y_values = predictions['OZONE']
                                x_values = []
                                for i in range(0, 24):
                                    x_values.append(str(i).zfill(2))
                                fig_ozone = go.Figure([go.Scatter(x=list(x_values), y=y_values, mode='lines')])
                                fig_ozone.update_layout(title="Quantity of O3 in Air" , xaxis_title='OZONE', yaxis_title="PPB")
                                st.plotly_chart(fig_ozone)
                            elif el == "NO2":
                                y_values = predictions['NO2']
                                x_values = []
                                for i in range(0, 24):
                                    x_values.append(str(i).zfill(2))
                                fig_no2 = go.Figure([go.Scatter(x=list(x_values), y=y_values, mode='lines')])
                                fig_no2.update_layout(title="Quantity of NO2 in Air" , xaxis_title='NO2', yaxis_title="PPB")
                                st.plotly_chart(fig_no2)
                            elif el == "SO2":
                                y_values = predictions['SO2']
                                x_values = []
                                for i in range(0, 24):
                                    x_values.append(str(i).zfill(2))
                                fig_so2 = go.Figure([go.Scatter(x=list(x_values), y=y_values, mode='lines')])
                                fig_so2.update_layout(title="Quantity of SO2 in Air" , xaxis_title='SO2', yaxis_title="PPB")
                                st.plotly_chart(fig_so2)
                            elif el == "CO":
                                y_values = predictions['CO']
                                x_values = []
                                for i in range(0, 24):
                                    x_values.append(str(i).zfill(2))
                                fig_co = go.Figure([go.Scatter(x=list(x_values), y=y_values, mode='lines')])
                                fig_co.update_layout(title="Quantity of CO in Air" , xaxis_title='CO', yaxis_title="PPM")
                                st.plotly_chart(fig_co)
                            elif el == "PM2.5":
                                y_values = predictions['PM2.5']
                                x_values = []
                                for i in range(0, 24):
                                    x_values.append(str(i).zfill(2))
                                fig_pm2_5 = go.Figure([go.Scatter(x=list(x_values), y=y_values, mode='lines')])
                                fig_pm2_5.update_layout(title="Quantity of PM2.5 in Air" , xaxis_title='PM2.5', yaxis_title="UG/M3")
                                st.plotly_chart(fig_pm2_5)
                            elif el == "PM10":
                                y_values = predictions['PM10']
                                x_values = []
                                for i in range(0, 24):
                                    x_values.append(str(i).zfill(2))
                                fig_pm10 = go.Figure([go.Scatter(x=list(x_values), y=y_values, mode='lines')])
                                fig_pm10.update_layout(title="Quantity of PM10 in Air" , xaxis_title='PM10', yaxis_title="UG/M3")
                                st.plotly_chart(fig_pm10)
                    elif result.status_code == 503:
                        st.error("API limit reached")

                        

def generate_openai_result(ozone_value):
    aqi = random.randint(36, 40)

    parameter = "ozone"
    #setting the API KEY here
    openai.api_key = os.environ.get('OPEN_AI_API_KEY')
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages = [
        {'role': 'user', 'content': "I am an air quality expert. Answer the below in less than 50 words as an air quality expert: what are effects of AQI {} {} what range is it in and what are the effects on health?".format(aqi, parameter)}
    ],
    temperature = 0.10)

    response  = completion.choices[0].message.content
    return response