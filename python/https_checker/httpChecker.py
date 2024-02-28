import requests
import sys




# Gets a list of Domains along with all the sub domains to check
def checkHTTP(domains, subdomains=[], only_show_http=True):
    url_list = []
    error_list = []

    for domain in domains:
        for subdomain in subdomains:
            current_url = {}
            if(subdomain):
                current_url['source_domain'] = subdomain + '.' + domain
            else:
                current_url['source_domain'] = domain

            print(current_url['source_domain'])
            
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
                if url_parts[0] == 'http:' and url_parts[1] == current_url['source_domain'] :
                    url_list.append(current_url)

            else:
                url_list.append(current_url)
            
            if current_url['final_url'] == "Error":
                error_list.append(current_url)
    
    # Print the results
    print("\nDomains Accessible by HTTP: \n")
    for url in url_list:
        print('{:<35}   -->  {:<25} \n'.format(url['source_domain'], url['final_url']))

    print("Domains That gave errors: \n")
    for url in error_list:
        print('{:<35}   -->  {:<25} \n'.format(url['source_domain'], url['final_url']))
    
        
        
# Default Domain List
domain_list = ["cmls.ca","abovecondos.com",'thewebley.com']

# Get text file name from arguments and read in domains
if len( sys.argv ) > 1:
    file = open(sys.argv[1], "r")
    domain_list = []
    for line in file:
        domain_list.append(line.strip())

# Subdomain list to check
# subdomain_list = ['','www',]
subdomain_list = ['www',]

# Check the domains
print("Checking Domains:")
checkHTTP(domain_list, subdomains=subdomain_list, only_show_http=True)