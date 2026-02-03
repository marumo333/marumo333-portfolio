import os

from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from supabase import Client, create_client

from schemas import CareerResponse, ProductsResponse, ProfileResponse, SkillsResponse

load_dotenv()

url: str | None = os.environ.get("SUPABASE_URL")
key: str | None = os.environ.get("SUPABASE_KEY")

assert url is not None, "SUPABASE_URL environment variable is not set"
assert key is not None, "SUPABASE_KEY environment variable is not set"

supabase: Client = create_client(url, key)

router = APIRouter(prefix="/api", tags=["profile"])


@router.get("/profile/me", response_model=ProfileResponse)
def get_portfolio() -> ProfileResponse:
    """Prile一覧を取得"""
    try:
        response = supabase.table("profiles").select("*").limit(1).single().execute()
        return ProfileResponse.model_validate(response.data)
    except Exception as e:
        print(f"Error:{e}")
        raise HTTPException(status_code=404, detail="Profile not found") from e


@router.get("/skills", response_model=list[SkillsResponse])
def get_skills() -> list[SkillsResponse]:
    """スキル一覧を取得"""
    try:
        response = supabase.table("skills").select("*").order("display_order").execute()
        return [SkillsResponse.model_validate(item) for item in response.data]
    except Exception as e:
        print(f"Error fetching skills: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch skills") from e


@router.get("/careers", response_model=list[CareerResponse])
def get_careers() -> list[CareerResponse]:
    """経歴一覧を取得"""
    try:
        # display_order の昇順で取得（または period_start の降順など）
        response = (
            supabase.table("careers").select("*").order("display_order").execute()
        )
        return [CareerResponse.model_validate(item) for item in response.data]
    except Exception as e:
        print(f"Error fetching careers: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch careers") from e


@router.get("/products", response_model=list[ProductsResponse])
def get_products() -> list[ProductsResponse]:
    """プロダクト一覧を取得"""
    try:
        # display_order の昇順で取得
        response = (
            supabase.table("products").select("*").order("display_order").execute()
        )
        return [ProductsResponse.model_validate(item) for item in response.data]
    except Exception as e:
        print(f"Error fetching products: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch products") from e
