const ipForm = document.getElementById("ip-form");
const detectForm = document.getElementById("detect-form");
const loader = document.getElementById("loader");
const resultContainer = document.getElementById("result-container");
const mapContainer = document.getElementById("map");

let map; 
let marker;

function fetchIPData(ip = null, detect = false) {
    loader.style.display = "block";
    resultContainer.innerHTML = "";
    
    if(map) map.remove(); 
    mapContainer.innerHTML = ""; 

    let formData = new FormData();
    if (detect) {
        formData.append("detect_ip", "1");
    } else {
        formData.append("ip", ip);
    }

    fetch("/", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        loader.style.display = "none";

        if(data.status === "success"){
            resultContainer.innerHTML = `
                <div class="card">
                    <h3>Result:</h3>
                    <p><b>IP:</b> ${data.query}</p>
                    <p><b>Country:</b> ${data.country}</p>
                    <p><b>City:</b> ${data.city}</p>
                    <p><b>ISP:</b> ${data.isp}</p>
                    <p><b>Timezone:</b> ${data.timezone}</p>
                </div>
            `;

            map = L.map('map').setView([data.lat, data.lon], 13);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 19,
                attribution: '© OpenStreetMap'
            }).addTo(map);

            let icon = L.divIcon({
                className: 'pulsating-marker'
            });

            marker = L.marker([data.lat, data.lon], {icon: icon}).addTo(map);
            marker.bindPopup(`
                <b>IP:</b> ${data.query}<br>
                <b>City:</b> ${data.city}<br>
                <b>Country:</b> ${data.country}<br>
                <b>ISP:</b> ${data.isp}
            `).openPopup();

        } else {
            resultContainer.innerHTML = `<p class="error">❌ Invalid IP address!</p>`;
        }
    })
    .catch(err => {
        loader.style.display = "none";
        resultContainer.innerHTML = `<p class="error">❌ Something went wrong!</p>`;
        console.error(err);
    });
}

ipForm.addEventListener("submit", function(e){
    e.preventDefault();
    const ip = document.getElementById("ip-input").value;
    if(ip) fetchIPData(ip, false);
});

detectForm.addEventListener("submit", function(e){
    e.preventDefault();
    fetchIPData(null, true);
});
