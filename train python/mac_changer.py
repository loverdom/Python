import subprocess
import optparse
import re
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help = "Interface to change it`s MAC address")
    parser.add_option("-m", "--mac", dest = "new_mac", help = "New MAC address")
    options, arguments = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options    

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for {0} to {1}".format(interface, new_mac))
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search:
        return mac_address_search.group(0)
    else:
        print("`[-] Could not to read MAC address.")    




options = get_arguments()
cur_mac = get_current_mac(options.interface)
print("Current MAC address: {0}".format(str(cur_mac)))

change_mac(options.interface, options.new_mac)

cur_mac = get_current_mac(options.interface)
if cur_mac == options.new_mac:
    print("[+] MAC address was successfully changed to {0}".format(str(cur_mac)))
else:
    print("[-] MAC address did not get changed.")    

