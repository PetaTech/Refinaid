from pydantic import BaseModel, Field
from typing import Literal


class Titanic(BaseModel):
    """Titanic dataset Columns.
    args:
        passenger_id: int
        survived: int
        p_class: int
        name: str
        sex: str
        age: float
        sib_sp: int
        parch: int
        ticket: str
        fare: float
        cabin: str
        embarked: str

    see:
        https://www.kaggle.com/datasets/yasserh/titanic-dataset/data
    """

    passenger_id: int | None = Field(alias="PassengerId")
    survived: int | None = Field(alias="Survived")
    p_class: int | None = Field(alias="Pclass")
    name: str | None = Field(alias="Name")
    sex: Literal["male", "female"] | None = Field(alias="Sex")
    age: float | None = Field(alias="Age")
    sib_sp: int | None = Field(alias="SibSp")
    parch: int | None = Field(alias="Parch")
    ticket: str | None = Field(alias="Ticket")
    fare: float | None = Field(alias="Fare")
    cabin: str | None = Field(alias="Cabin")
    embarked: str | None = Field(alias="Embarked")


class TitanicNumeric(BaseModel):
    """Titanic dataset Columns (Numeric).

    args:
        passenger_id: int
        p_class: int
        age: float
        sib_sp: int
        parch: int
        fare: float
    """

    passenger_id: int = Field(alias="PassengerId")
    p_class: int = Field(alias="Pclass")
    age: float = Field(alias="Age")
    sib_sp: int = Field(alias="SibSp")
    parch: int = Field(alias="Parch")
    fare: float = Field(alias="Fare")


def get_dataset_x_columns(dataset: str) -> list:
    dataset_columns = {
        "Titanic": [
            "PassengerId",
            "Pclass",
            "Sex",
            "Age",
            "SibSp",
            "Parch",
            "Ticket",
            "Fare",
            "Cabin",
            "Embarked",
        ],
        "House Prices": [
            "Id",
            "MSSubClass",
            "MSZoning",
            "LotFrontage",
            "LotArea",
            "Street",
            "Alley",
            "LotShape",
            "LandContour",
            "Utilities",
            "LotConfig",
            "LandSlope",
            "Neighborhood",
            "Condition1",
            "Condition2",
            "BldgType",
            "HouseStyle",
            "OverallQual",
            "OverallCond",
            "YearBuilt",
            "YearRemodAdd",
            "RoofStyle",
            "RoofMatl",
            "Exterior1st",
            "Exterior2nd",
            "MasVnrType",
            "MasVnrArea",
            "ExterQual",
            "ExterCond",
            "Foundation",
            "BsmtQual",
            "BsmtCond",
            "BsmtExposure",
            "BsmtFinType1",
            "BsmtFinSF1",
            "BsmtFinType2",
            "BsmtFinSF2",
            "BsmtUnfSF",
            "TotalBsmtSF",
            "Heating",
            "HeatingQC",
            "CentralAir",
            "Electrical",
            "1stFlrSF",
            "2ndFlrSF",
            "LowQualFinSF",
            "GrLivArea",
            "BsmtFullBath",
            "BsmtHalfBath",
            "FullBath",
            "HalfBath",
            "BedroomAbvGr",
            "KitchenAbvGr",
            "KitchenQual",
            "TotRmsAbvGrd",
            "Functional",
            "Fireplaces",
            "FireplaceQu",
            "GarageType",
            "GarageYrBlt",
            "GarageFinish",
            "GarageCars",
            "GarageArea",
            "GarageQual",
            "GarageCond",
            "PavedDrive",
            "WoodDeckSF",
            "OpenPorchSF",
            "EnclosedPorch",
            "3SsnPorch",
            "ScreenPorch",
            "PoolArea",
            "PoolQC",
            "Fence",
            "MiscFeature",
            "MiscVal",
            "MoSold",
            "YrSold",
            "SaleType",
            "SaleCondition",
        ],
        "Diabetes": [
            "Pregnancies",
            "Glucose",
            "BloodPressure",
            "SkinThickness",
            "Insulin",
            "BMI",
            "DiabetesPedigreeFunction",
            "Age",
        ],
    }

    return dataset_columns.get(dataset)


def get_dataset_numeric_columns(dataset: str) -> list:
    dataset_columns = {
        "Titanic": ["PassengerId", "Pclass", "Age", "SibSp", "Parch", "Fare"],
        "House Prices": [
            "Id",
            "MSSubClass",
            "LotFrontage",
            "LotArea",
            "OverallQual",
            "OverallCond",
            "YearBuilt",
            "YearRemodAdd",
            "MasVnrArea",
            "BsmtFinSF1",
            "BsmtFinSF2",
            "BsmtUnfSF",
            "TotalBsmtSF",
            "1stFlrSF",
            "2ndFlrSF",
            "LowQualFinSF",
            "GrLivArea",
            "BsmtFullBath",
            "BsmtHalfBath",
            "FullBath",
            "HalfBath",
            "BedroomAbvGr",
            "KitchenAbvGr",
            "TotRmsAbvGrd",
            "Fireplaces",
            "GarageYrBlt",
            "GarageCars",
            "GarageArea",
            "WoodDeckSF",
            "OpenPorchSF",
            "EnclosedPorch",
            "3SsnPorch",
            "ScreenPorch",
            "PoolArea",
            "MiscVal",
            "MoSold",
            "YrSold",
        ],
        "Diabetes": [
            "Pregnancies",
            "Glucose",
            "BloodPressure",
            "SkinThickness",
            "Insulin",
            "BMI",
            "DiabetesPedigreeFunction",
            "Age",
        ],
    }

    return dataset_columns.get(dataset)
