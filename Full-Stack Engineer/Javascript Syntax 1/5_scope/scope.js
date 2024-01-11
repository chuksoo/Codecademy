// Blocks and Scope
const city = "New York City";

const logCitySkyline = () => {
  let skyscraper = "Empire State Building";
  return "The stars over the " + skyscraper + " in " + city;
};

console.log(logCitySkyline());

// Global Scope
const satellites = "The Moon";
const galaxys = "The Milky Way";
const starsz = "North Star";

const callMyNightSky = () => {
  return "Night Sky: " + satellites + ", " + starsz + ", and " + galaxys;
};

console.log(callMyNightSky());

// Block Scope
const logVisibleLightWaves = () => {
  const lightWaves = "Moonlight";
  console.log(lightWaves);
};

logVisibleLightWaves();
console.log(lightWaves);

// Scope Pollution
const satellite = "The Moon";
const galaxy = "The Milky Way";
let stars = "North Star";

const callMyNightSky_ = () => {
stars = "Sirius";
return "Night Sky: " + satellite + ", " + stars + ", " + galaxy;
};

console.log(callMyNightSky());
console.log(stars);

// Practice Good Scoping
const logVisibleLightWavesz = () => {
  let lightWaves = "Moonlight";
  let region = "The Arctic";
  // Add if statement here:
  if (region === "The Arctic") {
    let lightWaves = "Northern Lights";
    console.log(lightWaves);
  }
  console.log(lightWaves);
};

logVisibleLightWavesz();

