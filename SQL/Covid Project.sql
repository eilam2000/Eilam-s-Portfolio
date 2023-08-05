SELECT Location, date, total_cases, new_cases, total_deaths, population
FROM "CovidDeaths"
Order By 1,2

-- Looking at Total Cases vs Total Deaths
-- Show likelihood of dying if you contract covid in your country
SELECT location, date, total_cases, total_deaths, (total_deaths::numeric / total_cases::numeric)*100 AS DeathPercentage
FROM "CovidDeaths"
WHERE location = 'Israel'
ORDER BY 1,2

-- Looking at Total Cases vs Population
--Shows what percentage of population got covid

SELECT location, date, population, total_cases,(total_cases::numeric/population::numeric )*100 AS PercentPopulationInfected
FROM "CovidDeaths"
--WHERE location = 'Israel'
ORDER BY 1,2


-- Looking at Countries with Highest infection Rate compared to Pupulation

SELECT location, population, MAX(total_cases) as HighestInfectionCount, MAX((total_cases::numeric/population::numeric))*100 AS  PercentPopulationInfected
FROM "CovidDeaths"
--WHERE location = 'Israel'
GROUP BY location, population
ORDER BY PercentPopulationInfected DESC NULLS LAST


-- Showing Countries with Highest Death Count per Population

SELECT location, MAX(Total_deaths) as TotalDeathCount
FROM "CovidDeaths"
WHERE continent is not null 
GROUP BY location
ORDER BY TotalDeathCount DESC NULLS LAST


-- Showing Countries with Highest Death Count per Population By Continent

SELECT continent, MAX(Total_deaths) as TotalDeathCount
FROM "CovidDeaths"
WHERE continent is not null 
GROUP BY continent
ORDER BY TotalDeathCount DESC 


-- Global Numbers

SELECT SUM(new_cases) as total_cases, SUM(cast(new_deaths as int)) as total_deaths, 
SUM(cast(new_deaths as int))/SUM(New_cases)*100 as DeathPercentage
FROM "CovidDeaths"
WHERE continent is not null
ORDER BY 1,2


-- Looking at Total Population vs Vaccinations

SELECT
    dea.continent,
    dea.location,
    dea.date,
    dea.population,
    vac.new_vaccinations,
    SUM(CAST(vac.new_vaccinations AS int)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) AS RollingPeopleVaccinated
FROM
    "CovidDeaths" dea
JOIN
    "CovidVaccinations" vac ON dea.location = vac.location AND dea.date = vac.date
WHERE
    dea.continent IS NOT NULL
ORDER BY
    dea.location,
    dea.date;



-- USE CTE

With PopvsVac (Continent, Location, Date, Population, New_Vaccinations, RollingPeopleVaccinated)
as
(
SELECT
    dea.continent,
    dea.location,
    dea.date,
    dea.population,
    vac.new_vaccinations,
    SUM(CAST(vac.new_vaccinations AS int)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) AS RollingPeopleVaccinated
FROM
    "CovidDeaths" dea
JOIN
    "CovidVaccinations" vac ON dea.location = vac.location AND dea.date = vac.date
WHERE
    dea.continent IS NOT NULL
ORDER BY
    dea.location,
    dea.date
)
SELECT *, (RollingPeopleVaccinated/Population)*100
FROM PopvsVac



-- Temp Table #PercentPopulationVaccinated
(
Continent varchar(255),
Location varchar(255),
Date date,
Population numeric,
New_Vaccinations numeric,
RollingPeopleVaccinated numeric,
)



Insert into #PercentPopulationVaccinated
SELECT
    dea.continent,
    dea.location,
    dea.date,
    dea.population,
    vac.new_vaccinations,
    SUM(CAST(vac.new_vaccinations AS int)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) AS RollingPeopleVaccinated
FROM
    "CovidDeaths" dea
JOIN
    "CovidVaccinations" vac ON dea.location = vac.location AND dea.date = vac.date
WHERE
    dea.continent IS NOT NULL
--ORDER BY
    dea.location,
    dea.date

SELECT *, (RollingPeopleVaccinated/Population)*100
FROM PopvsVac
