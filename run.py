from kapwrapper import Wrapper
from kapwrapper.models import Subject,FundGroup

if __name__ == '__main__':
    kap_wrapper = Wrapper()
    #result = kap_wrapper.get_last_portfoy_url("33E5FED7E61F00EAE0530A4A622B2AEA")
    #print(result)
    #kap_wrapper.get_kap_oids()
    #resp = kap_wrapper.get("https://www.kap.org.tr/tr/fon-bilgileri/genel/tkf-tacirler-portfoy-hisse-senedi-fonu-hisse-senedi-yogun-fon")

    #resp = kap_wrapper.get_funds(FundGroup.YATIRIM_FONLARI)
    resp = kap_wrapper.get_last_portfoy_url('4028328c73a8657f0173c3947a7b1347',FundGroup.YATIRIM_FONLARI)

    print(resp)