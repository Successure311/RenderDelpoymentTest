async function loadData() {
  const res = await fetch("https://renderdelpoymenttest.onrender.com/data");
  const data = await res.json();

  document.getElementById("output").textContent =
    JSON.stringify(data, null, 2);
}

window.loadData = loadData;
