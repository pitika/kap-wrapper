from kapwrapper import Wrapper
from kapwrapper.models import Subject

if __name__ == '__main__':
    kap_wrapper = Wrapper()
    result = kap_wrapper.get_last_portfoy("33E5FED7E61F00EAE0530A4A622B2AEA")
    print(result)
    #kap_wrapper.get_kap_oids()
    #resp = kap_wrapper.get("https://www.kap.org.tr/tr/fon-bilgileri/genel/tkf-tacirler-portfoy-hisse-senedi-fonu-hisse-senedi-yogun-fon")

    #print(resp)