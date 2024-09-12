import requests

# Define the URL for the POST request
url = "https://mids.usna.edu/ITSD/mids/drgwq010$mids.actionquery"

# Define the headers to match the fetch request
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://mids.usna.edu",
    "Connection": "keep-alive",
    "Cookie": (
    "f5avraaaaaaaaaaaaaaaa_session_=ANHJOJEEHJANEMICILNDIIOJHDABJCLAEKBPOKBGNBJKPHFHNHPGAHIMLGNAKOMJCAIDINOPOLOMPIOIGGFAAKEHIOHBHLJCPNNNIODFANAPEFBDMGLNODKKKHLEGHMD; "
    "f5_cspm=1234; "
    "WSG$DRGWQ010$URL0=/ITSD/mids/drgwq010$.startup; "
    "WSG$DRGWQ010$CAP0=Schedules_-_Query_Midshipmen; "
    "WSG$DRGWQ010$URL2=/ITSD/mids/drgwq010$mids.queryview?K_MIDS_ID=75405&K_SECOF_ID=192277&P_ALPHA=&P_LAST_NAME=&P_MICO_CO_NBR=&P_SECOF_COOF_SEBLDA_AC_YR=&P_SECOF_COOF_SEBLDA_SEM=&P_SECOF_COOF_SEBLDA_BLK_NBR=&P_MAJOR_CODE=&P_NOMI_FORMATTED_NAME=&Z_EXECUTE_QUERY=&Z_START=1&Z_ACTION=&Z_CHK=20344; "
    "WSG$DRGWQ010$CAP2=Schedule; "
    "nmstat=52bc9eb2-453c-fbde-b4dd-016a5d700b28; "
    "_ga_LY79N0FLBS=GS1.1.1726143873.34.0.1726143875.0.0.0; "
    "_ga=GA1.2.370835373.1693503430; "
    "BIGipServermids_prod=!7SN3bqnBgD52l/hHrP/1DhKiDM7x/kFd3yjJKA2H6rAfJWSb0XoX6iGjFY/lHPPWkZ61xsh6WyL/qw==; "
    "f5avraaaaaaaaaaaaaaaa_session_=CMAHCHAPHDJMCGGEAJOKCAFEGHKHNILOKDINNLLNOCIDOEJDLBGNDENKHJBFPGILCMADCBDJBLEBKAJKPOEABLOHIOBJOEDKADJNPEKNHDAFHJNHMEKPIIKABMGBCOGI; "
    "_gid=GA1.2.1084454608.1726143874; "
    "OAMAuthnCookie_mids.usna.edu:443=HU660VVC90U7T3tzqSGm9oB15dfLA8JBz%2BoZY1%2FO9d6JuuLgrrFMms5mUvHseA2s14VQPUswzVLrsCHeeEVmcf%2B%2BkpnYgvrT5GaC3wJeRZRYLWp5RI91wJ7B1Y0yNJCBUNbgckLIx5868Eee6BD1dRODq9DN8YCzY8xnh3BFpMYSxwmbLzUkIdpXZMNxooOtaSljiGnUPTpktVAJv5XwwjNjZOb5J13vxwNDi5lvAoDJAfSV5q9ndlst9NmhAHEkd9ixAaIC1rhzKw3BmynjQHDf4sjZgmRnYhrIJCAiUrjo0ay%2FM3nxfq%2FWY4mwnyatwOjy8RpTDrKuc2fG0pDEqGqI3zhIN5zuSNeXmFY0Jn1%2FlEVd5gqa85s6QNfORPCryl51c0MzfH0sUOEx9xD52VzxbnVGstULsWK%2FPFgzerjWDLLIAebIoIZB8vH6YpgEAtfu02IVRGQ92JSBFkAmj4nXDEcU9m0NGedYGkMHaT0LVCAghDEVdEeV7zcSAorVVShWhWVGJIZyf0ZImrjtWPw2zdv%2BaRI5RfxlKLc9KwPvko7U8ognjJzoZ3f6ypLFUeHTJuFb6V%2BSIuOvjRwN0A%3D%3D"
), 

    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Priority": "u=0, i"
}



# Define the data to be sent in the POST request
data = {
    "P_ALPHA": input("Enter in desired alpha\n"),
    "P_LAST_NAME": "",
    "P_MICO_CO_NBR": "",
    "P_SECOF_COOF_SEBLDA_AC_YR": "2025",
    "P_SECOF_COOF_SEBLDA_SEM": "FALL",
    "P_SECOF_COOF_SEBLDA_BLK_NBR": "1",
    "P_MAJOR_CODE": "",
    "P_NOMI_FORMATTED_NAME": "",
    "Z_ACTION": "QUERY",
    "Z_CHK": "0"
}

# Send the POST request
response = requests.post(url, headers=headers, data=data, allow_redirects=True)

# Print the response status and content
if response.status_code == 200:
    print("Request was successful.")
    file_name = input("Enter the file name to save the response content (e.g., response.txt): ")
    
    # Save the response content to the specified file
    with open(file_name, 'w') as f:
        f.write(response.text)
else:
    print("Request failed.")
    print("Status code:", response.status_code)
    print("Response content:", response.text)
