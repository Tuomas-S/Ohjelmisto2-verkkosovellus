"use strict";
//At first make an object from all points that its key is the name of route and its value is all points along the origin and destination
const routes = {
  "koti->keskusta": [
    "koti-keskusta1",
    "koti-keskusta2",
    "koti-keskusta3",
    "koti-keskusta4",
    "koti-keskusta5",
    "koti-keskusta6",
    "koti-keskusta7",
  ],
  "koti->kellari": ["koti-kellari8", "koti-kellari9", "koti-kellari10"],
  "kellari->vaja": [
    "kellari-vaja11",
    "kellari-vaja12",
    "kellari-vaja13",
    "kellari-vaja14",
    "kellari-vaja15",
    "kellari-vaja16",
    "kellari-vaja17",
  ],
  "vaja->raunio": [
    "vaja-raunio18",
    "vaja-raunio19",
    "vaja-raunio20",
    "vaja-raunio21",
  ],
  "raunio->pelto": [
    "raunio-pelto22",
    "raunio-pelto23",
    "raunio-pelto24",
    "raunio-pelto25",
    "raunio-pelto26",
    "raunio-pelto27",
    "raunio-pelto28",
    "raunio-pelto30",
    "raunio-pelto31",
    "raunio-pelto32",
  ],
  "metsä->pelto": [
    "metsä-pelto33",
    "metsä-pelto34",
    "metsä-pelto35",
    "metsä-pelto36",
    "metsä-pelto37",
    "metsä-pelto38",
    "metsä-pelto39",
    "metsä-pelto40",
    "metsä-pelto41",
    "metsä-pelto42",
    "metsä-pelto43",
    "metsä-pelto44",
    "metsä-pelto45",
  ],
  "metsä->raunio": [
    "metsä-raunio46",
    "metsä-raunio47",
    "metsä-raunio48",
    "metsä-raunio49",
    "metsä-raunio50",
    "metsä-raunio51",
    "metsä-raunio52",
    "metsä-raunio53",
    "metsä-raunio54",
    "metsä-raunio55",
  ],
  "koti->metsä": [
    "koti-metsä56",
    "koti-metsä57",
    "koti-metsä58",
    "koti-metsä59",
    "koti-metsä60",
    "koti-metsä61",
  ],
  "keskusta->kauppa": [
    "keskusta-kauppa62",
    "keskusta-kauppa63",
    "keskusta-kauppa64",
    "keskusta-kauppa65",
    "keskusta-kauppa66",
    "keskusta-kauppa67",
    "keskusta-kauppa68",
    "keskusta-kauppa69",
  ],
  "kauppa->pelto": [
    "kauppa-pelto70",
    "kauppa-pelto71",
    "kauppa-pelto72",
    "kauppa-pelto73",
    "kauppa-pelto74",
    "kauppa-pelto75",
    "kauppa-pelto76",
    "kauppa-pelto77",
    "kauppa-pelto78",
    "kauppa-pelto79",
    "kauppa-pelto80",
    "kauppa-pelto81",
    "kauppa-pelto82",
    "kauppa-pelto83",
    "kauppa-pelto84",
    "kauppa-pelto85",
    "kauppa-pelto86",
    "kauppa-pelto87",
    "kauppa-pelto88",
  ],
  "keskusta->kuja": [
    "keskusta-kuja89",
    "keskusta-kuja90",
    "keskusta-kuja91",
    "keskusta-kuja92",
    "keskusta-kuja93",
    "keskusta-kuja94",
    "keskusta-kuja95",
    "keskusta-kuja96",
    "keskusta-kuja97",
    "keskusta-kuja98",
    "keskusta-kuja99",
    "keskusta-kuja100",
    "keskusta-kuja101",
  ],
  "kuja->varasto": [
    "kuja-varasto102",
    "kuja-varasto103",
    "kuja-varasto104",
    "kuja-varasto105",
    "kuja-varasto106",
    "kuja-varasto107",
    "kuja-varasto108",
    "kuja-varasto109",
    "kuja-varasto110",
    "kuja-varasto111",
    "kuja-varasto112",
    "kuja-varasto113",
    "kuja-varasto114",
  ],
  "keskusta->metsä": [
    "keskusta-metsä115",
    "keskusta-metsä116",
    "keskusta-metsä117",
    "keskusta-metsä118",
    "keskusta-metsä119",
    "keskusta-metsä120",
    "keskusta-metsä121",
  ],
};
// At first get cuurent location from backend(send request via fetch ):
function getcurrentlocation() {
  // try {
  //     const response=await fetch("");
  //     if (!response.ok){
  //         throw new Error("Failed to get current location");
  //     }
  //     const responsejson=await response.json();
  //     console.log(responsejson)
  //     return responsejson
  // }catch(error) {
  //     console.error("Current location error:",error.message);
  //     return error.message
  // }
  return "koti";
}
let currentlocation = getcurrentlocation();
function showCurrentLocationVisual(currentlocation1) {
  const labels = document.querySelectorAll(".loclable");
  for (const loclable of labels) {
    loclable.classList.remove("current-location");
    if (loclable.textContent.trim() === currentlocation1) {
      loclable.classList.add("current-location");
    }
  }
}
showCurrentLocationVisual(currentlocation);

function showDestinationLocationVisual(Destination1) {
  const labels = document.querySelectorAll(".loclable");
  for (const loclable of labels) {
    loclable.classList.remove("destination-class");
    if (loclable.textContent.trim() === Destination1) {
      loclable.classList.add("destination-class");
    }
  }
}
function getRoutePoints(start, end) {
  const key = `${start.trim()}->${end.trim()}`;
  return routes[key];
}
function changePointsStyle(array, delay = 100) {
  let step = 0;
  for (let points of array) {
    setTimeout(() => {
      const chosenpoint = document.getElementById(points);
      chosenpoint.classList.add("active-path");
    }, step * delay);
    step++;
  }
}
let destination = null;
function getDestination(event) {
  destination = event.currentTarget.textContent.trim();
  showDestinationLocationVisual(destination);
  console.log(destination);
  const allpoint = getRoutePoints(currentlocation, destination);
  changePointsStyle(allpoint, 100);
  return destination;
}

const allbuttons = document.querySelectorAll(".loclable");
console.log(allbuttons.length);
for (const buutton of allbuttons) {
  buutton.addEventListener("click", getDestination);
}
