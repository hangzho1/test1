

import requests, datetime
import os, copy
import hashlib
import yaml
import operator


os.environ['WORKSPACE'] = "/home/hangz/validation"
print(os.getenv('WORKSPACE'))
start_date = '09-25-2023'
end_date = '10-1-2023'
artifactory_url = "https://af01p-igk.devtools.intel.com/artifactory/platform_hero-igk-local/benchmark_test_result/"


def download_public_file_from_artifactory(file_url, dst_path):
    """
    Download file from artifactory, it only works on those public artifacts.
    :param file_url: file url on artifactory
    :param dst_path: local path
    :return:
    """
    filename = file_url.split('/')[-1]
    r = requests.get(file_url, auth=(os.environ['ATF_CREDENTIAL_USR'], os.environ['ATF_CREDENTIAL_PSW']))
    not os.path.exists(dst_path) and os.mkdir(dst_path)
    with open(os.path.join(dst_path, filename), "wb") as f:
        f.write(r.content)
    f.close()

def download_benchmark_json(base_url, start_date, end_date, dst_path, platform='cloud',ignore_release=True):
    """
    Download all session benchmark result btw start_data and end_date
    :param base_url: test result root folder in artifactory
    :param start_date: start time like '12-03'
    :param end_date: end time like '12-09'
    :param dst_path: local path
    :param platform: options: cloud, local and all
    :return:
    """
    date_list = []
    start_date = datetime.datetime.strptime(start_date, '%m-%d-%Y').date()
    end_date = datetime.datetime.strptime(end_date, '%m-%d-%Y').date()

    while start_date <= end_date:
        date_list.append(str(start_date.strftime('%m-%d-%Y')))
        start_date += datetime.timedelta(days=1)
    if not date_list:
        return

    customer = os.getenv('customer', 'main')

    r = requests.get(base_url, auth=(os.environ['ATF_CREDENTIAL_USR'], os.environ['ATF_CREDENTIAL_PSW'])).text
    selector = html.fromstring(r)
    for oneday in date_list:
        oneday = str(oneday)

        daily_in_page = selector.xpath('//a[starts-with(text(),{!r})]'.format("NEX-daily-release_" + oneday))
        if platform == 'cloud':
            loc_in_page = selector.xpath('//a[contains(text(),{!r}) and contains(text(),{!r}) and contains(text(),{!r})]'.format("cloud", oneday, 'release'))
            loc_in_page = loc_in_page + daily_in_page
        elif platform == 'local':
            if customer == 'main':
                loc_in_page = selector.xpath('//a[contains(text(),{!r}) and contains(text(),{!r}) and contains(text(),{!r})]'.format("main", oneday, 'release'))
                loc_in_page = loc_in_page + daily_in_page

            if customer == 'ali':
                loc_in_page = selector.xpath('//a[starts-with(text(),{!r})]'.format("ali_release_" + oneday))

            if customer == 'tencent':
                loc_in_page = selector.xpath('//a[starts-with(text(),{!r})]'.format("tencent_release_" + oneday))

        else:
            loc_in_page = selector.xpath(
                '//a[contains(text(),{!r}) and not(contains(text(),{!r}))]'.format(oneday, 'bug_verify'))

        for loc in loc_in_page:
            json_dir_url = '/'.join((base_url, loc.xpath('./text()')[0], 'execution/'))

            res = requests.get(json_dir_url, auth=(os.environ['ATF_CREDENTIAL_USR'], os.environ['ATF_CREDENTIAL_PSW'])).text
            selector2 = html.fromstring(res)
            loc_in_page2 = selector2.xpath('//pre/a')

            for loc_a in loc_in_page2:
                json_file_name = loc_a.xpath('./text()')[0]
                if '..' not in json_file_name:
                    if platform == 'cloud' and '_cloud.' in json_file_name:
                        json_dir = dst_path
                        not os.path.exists(json_dir) and os.mkdir(json_dir)
                        file_url = '/'.join((json_dir_url, json_file_name))
                        download_public_file_from_artifactory(file_url, json_dir)
                    if platform == 'local' and '_cloud.' not in json_file_name:
                        json_dir = dst_path
                        not os.path.exists(json_dir) and os.mkdir(json_dir)
                        file_url = '/'.join((json_dir_url, json_file_name))
                        download_public_file_from_artifactory(file_url, json_dir)
    if ignore_release:
        for oneday in date_list:
            oneday = str(oneday)

            if platform == 'cloud':
                loc_in_page = selector.xpath('//a[starts-with(text(),{!r})]'.format("cloud-" + oneday))
            elif platform == 'local':
                if customer == 'main':
                    loc_in_page = selector.xpath('//a[starts-with(text(),{!r})]'.format("main_" + oneday))
            else:
                loc_in_page = selector.xpath(
                    '//a[contains(text(),{!r}) and not(contains(text(),{!r}))]'.format(oneday, 'bug_verify'))

            for loc in loc_in_page:
                json_dir_url = '/'.join((base_url, loc.xpath('./text()')[0], 'execution/'))

                res = requests.get(json_dir_url, auth=(os.environ['ATF_CREDENTIAL_USR'], os.environ['ATF_CREDENTIAL_PSW'])).text
                selector2 = html.fromstring(res)
                loc_in_page2 = selector2.xpath('//pre/a')

                for loc_a in loc_in_page2:
                    json_file_name = loc_a.xpath('./text()')[0]
                    if '..' not in json_file_name:
                        json_dir = dst_path
                        not os.path.exists(json_dir) and os.mkdir(json_dir)
                        file_url = '/'.join((json_dir_url, json_file_name))
                        print("no start with release files, download_public_file_from_artifactory:\n{}\n{}".format(file_url,json_dir))
                        download_public_file_from_artifactory(file_url, json_dir)

local_session_folder = os.path.join(os.environ['WORKSPACE'], 'local_release')
if not os.path.exists(local_session_folder):
    os.system('mkdir -p %s' % local_session_folder)
download_benchmark_json(artifactory_url, start_date, end_date, local_session_folder, platform='local', ignore_release=False)