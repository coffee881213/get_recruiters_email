# define the urls
urls = [
    'https://www.51job.com/',
    'https://www.zhaopin.com/',
    'https://www.lagou.com/',
    'https://www.liepin.com/',
    'https://www.zhipin.com/',
    'https://www.linkedin.com/'
]


urls_with_filter = []
# set the default position name and region
position_name = '测试'
region = '深圳'

url_51job = 'https://search.51job.com/list/' + region + ',000000,0000,00,9,99,' + position_name + ',2,1.html'
url_zhaopin = 'https://sou.zhaopin.com/?jl=' + region + '&kw=' + position_name
url_lagou = 'https://www.lagou.com/jobs/list_' + position_name + '?labelWords=&fromSearch=true&suginput='
url_liepin = 'https://www.liepin.com/zhaopin/?key=' + position_name + '&dqs=' + region
url_zhipin = 'https://www.zhipin.com/job_detail/?query=' + position_name + '&city=' + region
url_linkedin = 'https://www.linkedin.com/jobs/search?keywords=' + position_name + '&location=' + region


urls_with_filter.append(url_51job)
urls_with_filter.append(url_zhaopin)
urls_with_filter.append(url_lagou)
urls_with_filter.append(url_liepin)
urls_with_filter.append(url_zhipin)
urls_with_filter.append(url_linkedin)


