#data to be imported
import requests
import bs4
import tkinter as tk
import plyer
import threading
import datetime


def get_html_data(url):
    data = requests.get(url)
    return data


def get_corona_detail_of_india():
    url= "https://www.worldometers.info/coronavirus/country/india/"
    html_data = get_html_data(url)
    bs=bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div=bs.find("div", class_="content-inner").find_all("div", id="maincounter-wrap")
    print(len(info_div))
    all_details= ""
    for block in info_div:
        count = block.find("div", class_="maincounter-number").get_text()
        text = block.find("h1").get_text()
        all_details = all_details + text + ":" + count

    return all_details
# creating a function for refreshing data from  website

def refresh():
    newdata = get_corona_detail_of_india()
    print("Refreshing...")
    mainLabel['text'] = newdata

#function for notification
def notify_me():
    while True:
        plyer.notification.notify(
            title ="COVID information of INDIA",
            message =get_corona_detail_of_india(),
            timeout =20

        )
        time.sleep(40)


# creating  gui:
root = tk.Tk()
root.geometry("900x800")
root.iconbitmap("icon.ico")
root.title("CORONA DATA TRACKER - INDIA")
root.configure(background="white")
f = ("poppins", 25 , "bold")

banner = tk.PhotoImage(file = "banner.png")
bannerLabel = tk.Label(root , image = banner)
bannerLabel.pack()
mainLabel = tk.Label(root, text=get_corona_detail_of_india(), font=f, bg="white")
mainLabel.pack()

reBtn = tk.Button(root, text="REFRESH", font=f, relief='solid', command=refresh)
reBtn.pack()

# create a new thread
th1 = threading.Thread(target=notify_me)
th1.setDaemon(True)
th1.start()


root.mainloop()



