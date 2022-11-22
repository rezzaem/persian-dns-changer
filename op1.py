from command_runner.elevate import elevate
from command_runner import command_runner


def main():
    exit_code, output = command_runner('netsh interface ipv4 delete dnsservers "wi-Fi" all')
    exit_code, output = command_runner('netsh interface ipv4 add dnsservers "Wi-Fi" address=78.157.42.100 index=1')
    exit_code, output = command_runner('netsh interface ipv4 add dnsservers "Wi-Fi" address=78.157.42.101 index=2')

if __name__ == '__main__':
    elevate(main)
