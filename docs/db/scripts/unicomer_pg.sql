CREATE TABLE "Menu" (
  "id" bigserial PRIMARY KEY,
  "descripcion" varchar NOT NULL
);

CREATE TABLE "MenuOptions" (
  "id" bigserial[pk],
  "option" varchar NOT NULL,
  "from_menu" bigint
);

CREATE TABLE "Users" (
  "id" bigserial PRIMARY KEY,
  "name" varchar NOT NULL,
  "lastname" varchar NOT NULL,
  "email" varchar NOT NULL,
  "password" binary(60),
  "created_at" timestamptz NOT NULL DEFAULT (now()),
  "with_menu" bigserial
);

CREATE TABLE "Accounts" (
  "id" bigserial PRIMARY KEY,
  "owner" bigint,
  "balance" bigint NOT NULL,
  "currency" varchar NOT NULL,
  "created_at" timestamptz NOT NULL DEFAULT (now())
);

CREATE TABLE "CreditCards" (
  "id" bigserial PRIMARY KEY,
  "card_number" int NOT NULL,
  "expiration_date" date NOT NULL,
  "cvc" int,
  "from_account" bigint
);

CREATE TABLE "Entries" (
  "id" bigserial PRIMARY KEY,
  "from_account" bigint NOT NULL,
  "amount" bigint NOT NULL,
  "created_at" timestamptz NOT NULL DEFAULT (now())
);

CREATE TABLE "Transfers" (
  "id" bigserial PRIMARY KEY,
  "from_account_id" bigint NOT NULL,
  "to_account_id" bigint NOT NULL,
  "amount" bigint NOT NULL,
  "created_at" timestamptz NOT NULL DEFAULT (now())
);

CREATE INDEX ON "Users" ("name");

CREATE INDEX ON "Users" ("lastname");

CREATE INDEX ON "Users" ("email");

CREATE INDEX ON "Accounts" ("owner");

CREATE INDEX ON "CreditCards" ("card_number");

CREATE INDEX ON "CreditCards" ("from_account");

CREATE INDEX ON "Entries" ("from_account");

CREATE INDEX ON "Transfers" ("from_account_id");

CREATE INDEX ON "Transfers" ("to_account_id");

CREATE INDEX ON "Transfers" ("from_account_id", "to_account_id");

COMMENT ON COLUMN "Entries"."amount" IS 'can be negative or positive';

COMMENT ON COLUMN "Transfers"."amount" IS 'must be positive';

ALTER TABLE "MenuOptions" ADD FOREIGN KEY ("from_menu") REFERENCES "Menu" ("id");

ALTER TABLE "Users" ADD FOREIGN KEY ("with_menu") REFERENCES "Menu" ("id");

ALTER TABLE "Accounts" ADD FOREIGN KEY ("owner") REFERENCES "Users" ("id");

ALTER TABLE "CreditCards" ADD FOREIGN KEY ("from_account") REFERENCES "Accounts" ("id");

ALTER TABLE "Entries" ADD FOREIGN KEY ("from_account") REFERENCES "Accounts" ("id");

ALTER TABLE "Transfers" ADD FOREIGN KEY ("from_account_id") REFERENCES "Accounts" ("id");

ALTER TABLE "Transfers" ADD FOREIGN KEY ("to_account_id") REFERENCES "Accounts" ("id");
