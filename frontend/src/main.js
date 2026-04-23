async function loadData() {
  const res = await fetch("http://192.168.0.250:3030/data");
  const data = await res.json();

  document.getElementById("output").textContent =
    JSON.stringify(data, null, 2);
}

window.loadData = loadData;
