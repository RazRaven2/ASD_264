BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "general_ledger_accounts" (
	"account_number"	INTEGER,
	"account_description"	VARCHAR(50) UNIQUE,
	PRIMARY KEY("account_number")
);
CREATE TABLE IF NOT EXISTS "invoice_line_items" (
	"invoice_id"	INTEGER NOT NULL,
	"invoice_sequence"	INTEGER NOT NULL,
	"account_number"	INTEGER NOT NULL,
	"line_item_amount"	DECIMAL(9, 2) NOT NULL,
	"line_item_description"	VARCHAR(100) NOT NULL,
	PRIMARY KEY("invoice_id","invoice_sequence"),
	FOREIGN KEY("account_number") REFERENCES "general_ledger_accounts"("account_number"),
	FOREIGN KEY("invoice_id") REFERENCES "invoices"("invoice_id")
);
CREATE TABLE IF NOT EXISTS "invoices" (
	"invoice_id"	INTEGER,
	"vendor_id"	INTEGER NOT NULL,
	"invoice_number"	VARCHAR(50) NOT NULL,
	"invoice_date"	DATE NOT NULL,
	"invoice_total"	DECIMAL(9, 2) NOT NULL,
	"payment_total"	DECIMAL(9, 2) NOT NULL DEFAULT 0,
	"credit_total"	DECIMAL(9, 2) NOT NULL DEFAULT 0,
	"terms_id"	INTEGER NOT NULL,
	"invoice_due_date"	DATE NOT NULL,
	"payment_date"	DATE,
	PRIMARY KEY("invoice_id" AUTOINCREMENT),
	FOREIGN KEY("terms_id") REFERENCES "terms"("terms_id"),
	FOREIGN KEY("vendor_id") REFERENCES "vendors"("vendor_id")
);
CREATE TABLE IF NOT EXISTS "terms" (
	"terms_id"	INTEGER,
	"terms_description"	VARCHAR(50) NOT NULL,
	"terms_due_days"	INTEGER NOT NULL,
	PRIMARY KEY("terms_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "vendors" (
	"vendor_id"	INTEGER,
	"vendor_name"	VARCHAR(50) NOT NULL UNIQUE,
	"vendor_address1"	VARCHAR(50),
	"vendor_address2"	VARCHAR(50),
	"vendor_city"	VARCHAR(50) NOT NULL,
	"vendor_state"	CHAR(2) NOT NULL,
	"vendor_zip_code"	VARCHAR(20) NOT NULL,
	"vendor_phone"	VARCHAR(50),
	"vendor_contact_last_name"	VARCHAR(50),
	"vendor_contact_first_name"	VARCHAR(50),
	"default_terms_id"	INTEGER NOT NULL,
	"default_account_number"	INTEGER NOT NULL,
	PRIMARY KEY("vendor_id" AUTOINCREMENT),
	FOREIGN KEY("default_account_number") REFERENCES "general_ledger_accounts"("account_number"),
	FOREIGN KEY("default_terms_id") REFERENCES "terms"("terms_id")
);
CREATE INDEX IF NOT EXISTS "invoices_invoice_date_ix" ON "invoices" (
	"invoice_date"	DESC
);
COMMIT;
