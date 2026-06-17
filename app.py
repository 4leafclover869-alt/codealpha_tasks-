from flask import Flask, render_template, jsonify
from scapy.all import AsyncSniffer, IP, TCP, UDP, ICMP

app = Flask(__name__)

# Store captured packets
packets = []

# Global sniffer object
sniffer = None


def process_packet(packet):
    """Process each captured packet"""

    if IP in packet:

        protocol = "OTHER"

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"

        packet_info = {
            "source": packet[IP].src,
            "destination": packet[IP].dst,
            "protocol": protocol,
            "length": len(packet)
        }

        packets.append(packet_info)

        # Keep only latest 100 packets
        if len(packets) > 100:
            packets.pop(0)

        print(packet_info)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/start", methods=["POST"])
def start_capture():
    global sniffer

    if sniffer is None:

        sniffer = AsyncSniffer(
            prn=process_packet,
            store=False
        )

        sniffer.start()

        print("Packet Capture Started")

    return jsonify({
        "status": "success",
        "message": "Capture Started"
    })


@app.route("/stop", methods=["POST"])
def stop_capture():
    global sniffer

    if sniffer is not None:
        sniffer.stop()
        sniffer = None

        print("Packet Capture Stopped")

    return jsonify({
        "status": "success",
        "message": "Capture Stopped"
    })


@app.route("/packets")
def get_packets():
    return jsonify(packets)


@app.route("/stats")
def stats():

    tcp_count = sum(
        1 for p in packets
        if p["protocol"] == "TCP"
    )

    udp_count = sum(
        1 for p in packets
        if p["protocol"] == "UDP"
    )

    icmp_count = sum(
        1 for p in packets
        if p["protocol"] == "ICMP"
    )

    return jsonify({
        "total_packets": len(packets),
        "tcp": tcp_count,
        "udp": udp_count,
        "icmp": icmp_count
    })


@app.route("/clear", methods=["POST"])
def clear_packets():
    packets.clear()

    return jsonify({
        "status": "success",
        "message": "Packets Cleared"
    })


if __name__ == "__main__":
    app.run(debug=True)