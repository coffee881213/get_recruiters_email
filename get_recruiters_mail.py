import requests
from bs4 import BeautifulSoup
import re
import datetime
import os

from settings import urls_with_filter



# # 51job website
# url_51job = 'https://search.51job.com/list/' + region + ',000000,0000,00,9,99,' + position_name + ',2,1.html'
# response_51job = requests.get(url_51job)
#
# if response_51job.status_code == 200:
#     soup_51job = BeautifulSoup(response_51job.text, 'lxml')
#     # get the e-mail of recruiter
#     for mail in soup_51job.find_all('span', attrs={'title': re.compile('@')}):
#         mail = mail.getText().strip()
#         # save e-mail in a text file
#         with open('51job.txt', 'a', encoding='utf-8') as file:
#             file.write(mail + '\n')

def get_email(url_with_filter):
    # get the request and parse the html
    res = requests.get(url_with_filter)
    soup = BeautifulSoup(res.text, 'html.parser')
    # get the email
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', str(soup))
    # filter emails by position and region
    #filtered_emails = [email for email in emails if position in email and region in email]
    # return the emails
    return emails



# create folder, create file,
def create_folder():
    now = datetime.datetime.now()
    folder_name = '{}{}{}_{}{}{}'.format(now.year, now.month, now.day, now.hour, now.minute, now.second)
    os.mkdir(folder_name)
    return folder_name

def create_file(url, folder_name):
    # create file
    website_name = (url.split('/')[2]).split('.')[1]
    file_name = '{}.txt'.format(website_name)
    file_path = os.path.join(folder_name, file_name)
    return file_path

def save_to_file(path, emails):
    # save the emails in the file
    with open(path, 'a') as f:
        for email in emails:
            print(email)
            f.write(email + '\n')

if __name__ == "__main__":
    folder = create_folder()
    for filtered_url in urls_with_filter:
         file_path = create_file(filtered_url, folder)
         emails = get_email(filtered_url)
         save_to_file(file_path, emails)
