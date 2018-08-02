# https://leetcode.com/problems/subdomain-visit-count/description/
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        count_domain_res = {}
        for cpd in cpdomains:
            cd = cpd.split(' ')
            count = int(cd[0])
            domain = cd[1]
            d_arr = domain.split('.')
            for i,d in enumerate(d_arr):
                url = '.'.join(d_arr[i:])
                if count_domain_res.get(url):
                    count_domain_res[url]=count_domain_res[url]+count
                else:
                    count_domain_res[url]=count
        res = []
        for k,v in count_domain_res.items():
            res.append("%s %s"%(v,k))
            
        return res

# dic = {}
# for domain in cpdomains:
# 	count, *domain = domain.replace(" ",".").split(".")
# 	for i in range(len(domain)):
# 		item = ".".join(domain[i:])
# 		if not item in dic: dic[item] = int(count)
# 		else: dic[item] += int(count)
# return [" ".join((str(v), k)) for k, v in dic.items()]