async function startCapture() {
    try {

        const response = await fetch("/start", {
            method: "POST"
        });

        const data = await response.json();

        alert(data.message);

    } catch (error) {
        console.error(error);
        alert("Failed to start packet capture");
    }
}

async function stopCapture() {
    try {

        const response = await fetch("/stop", {
            method: "POST"
        });

        const data = await response.json();

        alert(data.message);

    } catch (error) {
        console.error(error);
    }
}

async function clearPackets() {
    try {

        const response = await fetch("/clear", {
            method: "POST"
        });

        const data = await response.json();

        document.getElementById("count").innerText = "0";
        document.getElementById("packetTable").innerHTML = "";

        alert(data.message);

    } catch (error) {
        console.error(error);
    }
}

async function loadPackets() {

    try {

        const response = await fetch("/packets");
        const data = await response.json();

        document.getElementById("count").innerText = data.length;

        const table = document.getElementById("packetTable");

        table.innerHTML = "";

        data.forEach(packet => {

            table.innerHTML += `
                <tr>
                    <td>${packet.source}</td>
                    <td>${packet.destination}</td>
                    <td>${packet.protocol}</td>
                    <td>${packet.length}</td>
                </tr>
            `;
        });

    } catch (error) {
        console.error(error);
    }
}

async function loadStats() {

    try {

        const response = await fetch("/stats");
        const stats = await response.json();

        console.log("Stats:", stats);

    } catch (error) {
        console.error(error);
    }
}

setInterval(() => {
    loadPackets();
    loadStats();
}, 1000);

window.onload = () => {
    loadPackets();
    loadStats();
};