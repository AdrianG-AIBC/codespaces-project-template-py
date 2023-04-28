from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class LogoImage(BaseModel):
    id: str
    size: int
    filetype: str
    originalname: str
    path: str


class Platform(BaseModel):
    thehub: bool
    plusimpact: bool


class RecommendedBy(BaseModel):
    name: Optional[str] = None
    website: Optional[str] = None


class SlackNotifications(BaseModel):
    jobCreated: bool
    jobEnded: bool
    applicationCreated: bool
    applicationCommented: bool


class Location(BaseModel):
    address: str
    locality: str
    route: str
    postalCode: str
    country: str


class Center(BaseModel):
    type: str
    _id: str
    coordinates: List[float]


class Bounds(BaseModel):
    type: str
    _id: str
    coordinates: List[List[List[float]]]


class GeoLocation(BaseModel):
    center: Center
    bounds: Optional[Bounds] = None


class Country(BaseModel):
    countryCode: str
    location: Location
    geoLocation: GeoLocation
    registrationNumber: str
    status: str
    createdAt: Optional[str] = None


class Plusimpact(BaseModel):
    status: str


class Views(BaseModel):
    week: int
    total: int


class Doc(BaseModel):
    id: str
    key: str
    name: str
    logoImage: LogoImage
    whatWeDo: str
    website: str
    numberOfEmployees: str
    founded: str
    perks: List[str]
    stage: Optional[str] = None
    funding: str
    fundingStage: Optional[str] = None
    numberOfActiveJobs: int
    createdAt: str
    isImpact: bool
    platform: Platform
    wasRecommended: bool
    recommendedBy: RecommendedBy
    slackNotifications: SlackNotifications
    externalDomain: Optional[str] = None
    sdgs: List[str]
    industries: List[str]
    businessModels: List[str]
    countries: List[Country]
    followed: bool
    unbounceGroup: int
    plusimpact: Plusimpact
    views: Views
    slack: bool
    video: Optional[str] = None
    market: Optional[str] = None


class Countries(BaseModel):
    dk: int
    se: int
    no: int
    fi: int
    ni: int


class Industries(BaseModel):
    consumergoods: int
    education: int
    greentech: int
    entertainment: int
    fintech: int
    healthcare: int
    itsoftware: int
    maritime: int
    saas: int
    service: int
    marketplace: int
    manufacturing: int
    telecommunications: int
    retail: int
    agriculture: int
    food: int
    science: int
    travel: int
    sports: int
    advertising: int
    sales: int
    fashion: int
    hospitality: int
    robotics: int
    legal: int
    jobs: int
    gaming: int
    iot: int
    music: int
    blockchain: int


class Stages(BaseModel):
    growth: int
    idea: int
    goToMarket: int
    prototype: int


class NumberOfEmployees(BaseModel):
    field_51_100: int = Field(..., alias="51-100")
    field_11_50: int = Field(..., alias="11-50")
    field_101_200: int = Field(..., alias="101-200")
    field_1_10: int = Field(..., alias="1-10")
    field_200_: int = Field(..., alias="200+")


class Funding(BaseModel):
    notLooking: int
    funded: int
    looking: int


class Impact(BaseModel):
    true: int
    false: int


class FundingStage(BaseModel):
    seed: int
    seriesa: int
    ipo: int
    preseed: int
    bootstrapping: int
    seriesb: int


class Market(BaseModel):
    both: int
    developed: int
    emerging: int


class Sdgs(BaseModel):
    noPoverty: int
    zeroHunger: int
    goodHealth: int
    qualityEducation: int
    genderEquality: int
    cleanWater: int
    cleanEnergy: int
    economicGrowth: int
    industry: int
    reducedInequalities: int
    suistainableCities: int
    responsibleConsumption: int
    climateAction: int
    lifeBelowWater: int
    lifeOnLand: int
    peace: int
    partnerships: int


class Suggestions(BaseModel):
    countries: Countries
    industries: Industries
    stages: Stages
    numberOfEmployees: NumberOfEmployees
    funding: Funding
    impact: Impact
    fundingStage: FundingStage
    market: Market
    sdgs: Sdgs


class Model(BaseModel):
    docs: Optional[List[Doc]] = None
    total: Optional[int] = None
    limit: Optional[int] = None
    page: Optional[str] = None
    pages: Optional[int] = None
    suggestions: Optional[Suggestions] = None
