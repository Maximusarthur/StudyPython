import requests
import xlwt
from bs4 import BeautifulSoup

DATALIST_SIZE = 30
SAVE_PATH = "招聘信息.xls"
URL = 'https://km.58.com/tech/pn'

HEADERS = {
    "User-Agent": "Mozilla / 5.0(Windows NT 11.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.123  Safari / 537.36"
}
COOKIES = {'58cooper': "userid=96120537671444&username=9ym5nog32"}


def fetch_html(url):
    response = requests.get(url, headers=HEADERS, cookies=COOKIES)
    if response.status_code == 200:
        return response.text
    return None


def extract_job_titles(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('li', class_='job_item clearfix')
    titles = []
    for item in items:
        title_need = item.find('span', class_='name')
        title_name = item.find('span', class_='cate')
        title_company = item.find('div', class_='comp_name')
        title_xueli = item.find('span', class_='xueli')
        title_jingyan = item.find('span', class_='jingyan')
        title_salary = item.find('p',class_='job_salary')
        if title_need:
            title = title_need.text.strip()
            name = title_name.text.strip()
            company = title_company.text.strip()
            xueli = title_xueli.text.strip()
            jingyan = title_jingyan.text.strip()
            salary = title_salary.text.strip()
            titles.append(title)
            titles.append(name)
            titles.append(company)
            titles.append(xueli)
            titles.append(jingyan)
            titles.append(salary)
    return titles


def save_to_excel(job_data, save_path):
    try:
        book = xlwt.Workbook(encoding="utf-8", style_compression=0)
        sheet = book.add_sheet('招聘', cell_overwrite_ok=True)
        col = ("需求", "名称", "公司", "学历", "经验","薪资")
        for i in range(len(col)):
            sheet.write(0, i, col[i])

        row = 1
        for i in range(0, len(job_data), 6):
            sheet.write(row, 0, job_data[i])
            sheet.write(row, 1, job_data[i + 1])
            sheet.write(row, 2, job_data[i + 2])
            sheet.write(row, 3, job_data[i + 3])
            sheet.write(row, 4, job_data[i + 4])
            sheet.write(row, 5, job_data[i + 5])
            row += 1

        book.save(save_path)
    except Exception as e:
        print(f"Error saving to Excel: {e}")


def main():
    all_job_titles = []
    for i in range(1, 301):
        html = fetch_html(URL + str(i))
        if html:
            job_titles = extract_job_titles(html)
            all_job_titles.extend(job_titles)

    save_to_excel(all_job_titles, SAVE_PATH)


if __name__ == "__main__":
    print("saving......")
    main()
