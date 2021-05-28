import cgi
from mechanize import Browser, _http
import http.cookiejar as cookielib
from keep_your_secrets import keep_your_secrets as kp

def tecnec_dwnld():
    data_url = kp()[5]
    site = kp()[6]

    # Browser
    br = Browser()

    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    # Browser options
    br.set_handle_equiv(True)
    #br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(_http.HTTPRefreshProcessor(), max_time=1)

    # User-Agent (this is cheating, ok?)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0')]

    # The site we will navigate into, handling it's session
    response = br.open(data_url)
    html = response.get_data()
    br.select_form(nr=2)

    # User credentials
    br.form['ctl00$body$txtEmail'] = kp()[7]
    br.form['ctl00$body$txtPassword'] = kp()[8]
    br.submit()

    #Open Dealer Resources Page
    br.open(site)

    #Creating List Variables for Future Use
    filetypes = ["xls", "xlsx", ]
    myfiles = []
    urls = [kp()[9], kp()[10]]

    # Iterate through all links for results that contain any string contained in the filetypes list and add ALL link data
    # for matches to the blank myfiles list we made before
    for l in br.links():
        myfiles.extend([l for t in filetypes if t in l.url or t in l.text])


    # Iterate through the myfiles list, and retrieve the files from the url attribute and assign them the name which
    # matches the attribute filename contained in the Content Disposition response header

    for l in myfiles:
        if l.url not in urls:
            test = br.open(l.url)
            info = test.info()
            header = info.get('Content-Disposition')
            value, params = cgi.parse_header(header)
            filename = '/home/filestore/' + params['filename']
            br.retrieve(l.url, filename)

