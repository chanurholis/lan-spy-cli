# lan_spy/main.py

import click


# 1. Perintah untuk Scan (Pencarian Host)
@click.command()
def scan():
    """Memindai jaringan LAN untuk host yang aktif."""
    click.echo("Memulai pemindaian host LAN...")
    # Panggil fungsi dari host_scanner.py di sini


# 2. Perintah untuk Ports (Port Scanning)
@click.command()
@click.argument("target_ip")
def ports(target_ip):
    """Memindai port yang terbuka pada IP target."""
    click.echo(f"Memindai port pada IP: {target_ip}...")
    # Panggil fungsi dari port_scanner.py di sini


# 3. Perintah untuk Sniff (Traffic Sniffing)
@click.command()
@click.option(
    "--interface", default=None, help="Interface jaringan yang akan digunakan."
)
def sniff(interface):
    """Menganalisis lalu lintas jaringan (membutuhkan izin root/admin)."""
    click.echo(
        f"Menganalisis traffic pada interface: {interface or 'auto'}. Ini memerlukan izin admin."
    )
    # Panggil fungsi dari traffic_sniffer.py di sini


# Grup Utama
@click.group()
def cli():
    """
    LAN Spy CLI: Tools untuk memantau jaringan LAN, host, port, dan traffic.
    Cocok untuk Hacktoberfest!
    """
    pass


# Menambahkan Perintah ke Grup
cli.add_command(scan)
cli.add_command(ports)
cli.add_command(sniff)

if __name__ == "__main__":
    cli()
