from main.repository.monitor import Monitor


def run():
    server_ip_address = "3.89.135.227"
    port = 22
    username = "interfadm"
    password = "Projet654!"
    monitor = Monitor(server_ip_address, username, password)
    monitor.connect_ssh()
