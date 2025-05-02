from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import (
    info_card,
    user,
    line_status,
    raw_stock,
    finished_stock,
    production_plan
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(info_card.router, prefix="/info", tags=["Info Cards"])
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(line_status.router, prefix="/line_status",
                   tags=["Cache: Line Status"])
app.include_router(raw_stock.router, prefix="/raw_stock",
                   tags=["Cache: Raw Stock"])
app.include_router(finished_stock.router, prefix="/finished_stock",
                   tags=["Cache: Finished Goods"])
app.include_router(production_plan.router, prefix="/production_plan",
                   tags=["Cache: Production Plan"])


@app.get("/health")
def health():
    return {"message": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
