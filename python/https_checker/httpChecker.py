import requests

# Gets a list of Domains along with all the sub domains to check
def checkHTTP(domains, subdomains=[], only_show_http=True):
    url_list = []

    for domain in domains:
        for subdomain in subdomains:
            current_url = {}
            if(subdomain):
                current_url['source_domain'] = subdomain + '.' + domain
            else:
                current_url['source_domain'] = domain
            
            try:
                response = requests.get('http://' + current_url['source_domain'], timeout=5)

                # Check if history is empty
                if(response.history):
                    current_url['redirects'] = len(response.history)
                
                current_url['final_url'] = response.url

            except:
                current_url['final_url'] = "Error"
            
            # Check if we only want to save HTTP urls and Errors
            if only_show_http:
                url_parts = list(filter(None,current_url['final_url'].split('/')))
                if (url_parts[0] == 'http:' and url_parts[1] == current_url['source_domain']) or current_url['final_url'] == "Error":
                    url_list.append(current_url)

            else:
                url_list.append(current_url)
    
    # Print the results
    print()
    for url in url_list:
        print(url)
        print()
    
        
        

domain_list = ["cmls.ca","abovecondos.com",'thewebley.com']
subdomain_list = ['','www',]

checkHTTP(domain_list, subdomains=subdomain_list, only_show_http=True)