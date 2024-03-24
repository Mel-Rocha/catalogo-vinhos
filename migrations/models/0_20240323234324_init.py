from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "wine" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "nation" VARCHAR(50),
    "type" VARCHAR(50),
    "grape_variety" VARCHAR(100),
    "region" VARCHAR(100),
    "production" VARCHAR(100),
    "area" VARCHAR(100),
    "vintage" VARCHAR(10),
    "format" VARCHAR(10),
    "gradation" VARCHAR(10),
    "service" VARCHAR(100),
    "temperature" VARCHAR(10),
    "combination" VARCHAR(200),
    "dosage" VARCHAR(50),
    "method" VARCHAR(50),
    "producer" VARCHAR(100),
    "tasting_notes" TEXT
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
