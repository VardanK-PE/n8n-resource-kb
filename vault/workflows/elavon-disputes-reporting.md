---
n8n_id: "haux7wgQdkCwNqP6"
name: "Elavon Disputes Reporting"
status: inactive
last_modified: 2026-03-16T17:47:17.408Z
tags: []
fingerprint: "f802af14c5017811e42d493e42b0b7fa08ad06af476769a24ecf5fa408404db0"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Elavon Disputes Reporting

## Summary

- **Status:** inactive
- **n8n ID:** `haux7wgQdkCwNqP6`
- **Nodes:** 133
- **Last modified:** 2026-03-16T17:47:17.408Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `7c7b9f8f-eca1-4ae4-bdc7-5f39a4a1cab0`)
- **schedule** — node "Schedule Trigger" (id `905a6066-6d3c-4222-9c85-dae43d5f9e22`) — `daily at 8:00`
- **execute-workflow** — node "When Executed by Another Workflow" (id `b8416af3-dc4b-4806-87f1-7884656df532`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Emails Sent to Elavon" (id `197f0d0f-208a-41dd-8f47-5662102c1582`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet1" (id `19bba2f7-105c-44fb-a710-e685014c889b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Delete rows or columns from sheet" (id `1a07e383-a0c1-424a-9e2c-fbb5c7ba98b4`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request attachment's payment transaction1" (id `1ffe5bda-a5ef-46aa-9da5-654a280cd384`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request PE Transactions for the last 24 hours1" (id `24f4a251-a9eb-467f-81aa-0799c5cfc0de`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Dispute Data2" (id `29d09005-6157-4873-976e-a246e9ee4023`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request PE Transactions for the last 24 hours6" (id `2d0da237-c427-415b-869e-de05dc386e71`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request refund transactions in ACD or AMR states1" (id `30affcfd-cf42-4816-a6b9-ebaba5bbcca6`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request PE Transactions for the last 24 hours3" (id `3abb3468-4332-49a0-8787-60f9998b3ea2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet2" (id `3e3e021c-2b38-40c2-aaea-346f804d4118`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get many messages5" (id `44c03d6a-8773-455c-abc2-f5d94395866e`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks1" (id `4e7db500-f29b-42f9-ba54-1dae4608e309`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Get many messages" (id `55466e28-dba4-44c2-ba7f-d6ea189139ac`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request attachment's payment transaction" (id `56b0635b-7499-4dd0-871a-1c013268478c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Dispute Data1" (id `57942192-35b8-4c08-84b5-7cbed15d04bb`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Get many messages1" (id `67bae9ba-3260-4257-a798-043f48957b93`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `67ee336b-2246-43b8-9659-25b3b9d89d6c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet3" (id `6f33219b-a869-4695-9bff-51ba69963b0f`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request refund transactions in ACD or AMR states2" (id `76e405d3-ad69-4a75-a1ec-9fb49ee1737c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet2" (id `7ecc1304-30ac-4bc8-93f2-795fcc1ebd4a`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request PE Transactions for the last 24 hours7" (id `86e9d6ee-56db-4f99-be28-a6d0ab510c75`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet1" (id `91dcd17a-4760-4fbd-ae8a-06738d53306a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PI Chargebacks - Processed" (id `99caf9a4-a39c-4b00-8fd8-2dff185b0776`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PI Chargebacks" (id `a274ec9a-ffdc-446a-8f09-50c14d118bbf`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request PE Transactions for the last 24 hours" (id `a39a3a67-aca1-4445-9fd0-086ccbe51338`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `ae357777-36c3-42c8-b38a-6664d99822d4`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks" (id `b65f1c26-5390-45e7-8d62-238731979e19`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PI Data" (id `ba9ec7fb-18ad-4613-8d09-f86d412e7089`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks2" (id `bbda295b-5286-44fd-b58b-b89b4a668626`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request refund transactions in ACD or AMR states3" (id `bcf96626-6827-4802-b854-38dcffe14a88`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Emails Sent to Elavon1" (id `bdb36ab7-2115-4de7-bd90-9f76aabb7b7c`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Get many messages4" (id `c8507fea-9ae9-450e-8078-dae8a9a460a1`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request PE Transactions for the last 24 hours4" (id `d63cdc8e-9f62-4e86-b583-62811f53bca9`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request PE Transactions for the last 24 hours5" (id `d6747f07-9783-4fc6-9625-fe2573b01427`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get many messages2" (id `d7e366a9-3b76-4f4b-b361-fb58c07282ff`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Get many messages3" (id `d9c5042c-b032-4544-b266-0ed22e92e779`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Dispute Attachments" (id `e1004686-5928-4d24-a86d-eb62d0a1cb03`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request PE Transactions for the last 24 hours2" (id `e5955cf5-47a0-4201-9be7-eec7822177f7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Dispute Attachments1" (id `e7494f03-e307-4b82-b165-dd966b33dfc1`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request refund transactions in ACD or AMR states" (id `fc172fc3-a4a1-4075-a4bb-e67378a099e6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet3" (id `fd125896-1862-4a1e-95a0-3487df69b92a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `ffa39e78-cbe5-4b47-835c-9d9943cdd39a`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request attachment's payment transaction1" (id `1ffe5bda-a5ef-46aa-9da5-654a280cd384`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request PE Transactions for the last 24 hours1" (id `24f4a251-a9eb-467f-81aa-0799c5cfc0de`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request PE Transactions for the last 24 hours6" (id `2d0da237-c427-415b-869e-de05dc386e71`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request refund transactions in ACD or AMR states1" (id `30affcfd-cf42-4816-a6b9-ebaba5bbcca6`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request PE Transactions for the last 24 hours3" (id `3abb3468-4332-49a0-8787-60f9998b3ea2`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks1" (id `4e7db500-f29b-42f9-ba54-1dae4608e309`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request attachment's payment transaction" (id `56b0635b-7499-4dd0-871a-1c013268478c`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request refund transactions in ACD or AMR states2" (id `76e405d3-ad69-4a75-a1ec-9fb49ee1737c`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request PE Transactions for the last 24 hours7" (id `86e9d6ee-56db-4f99-be28-a6d0ab510c75`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request PE Transactions for the last 24 hours" (id `a39a3a67-aca1-4445-9fd0-086ccbe51338`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks" (id `b65f1c26-5390-45e7-8d62-238731979e19`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks2" (id `bbda295b-5286-44fd-b58b-b89b4a668626`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request refund transactions in ACD or AMR states3" (id `bcf96626-6827-4802-b854-38dcffe14a88`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request PE Transactions for the last 24 hours4" (id `d63cdc8e-9f62-4e86-b583-62811f53bca9`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request PE Transactions for the last 24 hours5" (id `d6747f07-9783-4fc6-9625-fe2573b01427`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request PE Transactions for the last 24 hours2" (id `e5955cf5-47a0-4201-9be7-eec7822177f7`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request refund transactions in ACD or AMR states" (id `fc172fc3-a4a1-4075-a4bb-e67378a099e6`)

### Google Sheets

- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Disputes` — node "Emails Sent to Elavon" (id `197f0d0f-208a-41dd-8f47-5662102c1582`)
- [[../resources/google-sheets/1cltxfeklqgzgu-f3jj3i3wvviwplozhfujuefjzubas|Elavon dispute reporting]] (id `1cltxFEklqGZgu-F3jJ3i3wvvIwPLOzHFUjUefJZuBas`) — op `append`, tab `PI Change Log` — node "Append row in sheet1" (id `19bba2f7-105c-44fb-a710-e685014c889b`)
- [[../resources/google-sheets/1cltxfeklqgzgu-f3jj3i3wvviwplozhfujuefjzubas|Elavon dispute reporting]] (id `1cltxFEklqGZgu-F3jJ3i3wvvIwPLOzHFUjUefJZuBas`) — op `delete`, tab `Transactions PE` — node "Delete rows or columns from sheet" (id `1a07e383-a0c1-424a-9e2c-fbb5c7ba98b4`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Disputes` — node "Dispute Data2" (id `29d09005-6157-4873-976e-a246e9ee4023`)
- [[../resources/google-sheets/1cltxfeklqgzgu-f3jj3i3wvviwplozhfujuefjzubas|Elavon dispute reporting]] (id `1cltxFEklqGZgu-F3jJ3i3wvvIwPLOzHFUjUefJZuBas`) — op `appendOrUpdate`, tab `Summary V2` — node "Append or update row in sheet2" (id `3e3e021c-2b38-40c2-aaea-346f804d4118`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Disputes` — node "Dispute Data1" (id `57942192-35b8-4c08-84b5-7cbed15d04bb`)
- [[../resources/google-sheets/1cltxfeklqgzgu-f3jj3i3wvviwplozhfujuefjzubas|Elavon dispute reporting]] (id `1cltxFEklqGZgu-F3jJ3i3wvvIwPLOzHFUjUefJZuBas`) — op `appendOrUpdate`, tab `Transactions PE` — node "Append or update row in sheet" (id `67ee336b-2246-43b8-9659-25b3b9d89d6c`)
- [[../resources/google-sheets/1cltxfeklqgzgu-f3jj3i3wvviwplozhfujuefjzubas|Elavon dispute reporting]] (id `1cltxFEklqGZgu-F3jJ3i3wvvIwPLOzHFUjUefJZuBas`) — op `appendOrUpdate`, tab `Summary V2` — node "Append or update row in sheet3" (id `6f33219b-a869-4695-9bff-51ba69963b0f`)
- [[../resources/google-sheets/1cltxfeklqgzgu-f3jj3i3wvviwplozhfujuefjzubas|Elavon dispute reporting]] (id `1cltxFEklqGZgu-F3jJ3i3wvvIwPLOzHFUjUefJZuBas`) — op `append`, tab `PE Dispute Change Log` — node "Append row in sheet2" (id `7ecc1304-30ac-4bc8-93f2-795fcc1ebd4a`)
- [[../resources/google-sheets/1cltxfeklqgzgu-f3jj3i3wvviwplozhfujuefjzubas|Elavon dispute reporting]] (id `1cltxFEklqGZgu-F3jJ3i3wvvIwPLOzHFUjUefJZuBas`) — op `appendOrUpdate`, tab `Summary V2` — node "Append or update row in sheet1" (id `91dcd17a-4760-4fbd-ae8a-06738d53306a`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Chargebacks PI` — node "PI Chargebacks - Processed" (id `99caf9a4-a39c-4b00-8fd8-2dff185b0776`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `chargebacks` — node "PI Chargebacks" (id `a274ec9a-ffdc-446a-8f09-50c14d118bbf`)
- [[../resources/google-sheets/1cltxfeklqgzgu-f3jj3i3wvviwplozhfujuefjzubas|Elavon dispute reporting]] (id `1cltxFEklqGZgu-F3jJ3i3wvvIwPLOzHFUjUefJZuBas`) — op `append`, tab `Attachment Change Log` — node "Append row in sheet" (id `ae357777-36c3-42c8-b38a-6664d99822d4`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Chargebacks PI` — node "PI Data" (id `ba9ec7fb-18ad-4613-8d09-f86d412e7089`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Disputes` — node "Emails Sent to Elavon1" (id `bdb36ab7-2115-4de7-bd90-9f76aabb7b7c`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `?`, tab `emails` — node "Dispute Attachments" (id `e1004686-5928-4d24-a86d-eb62d0a1cb03`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `?`, tab `emails` — node "Dispute Attachments1" (id `e7494f03-e307-4b82-b165-dd966b33dfc1`)
- [[../resources/google-sheets/1cltxfeklqgzgu-f3jj3i3wvviwplozhfujuefjzubas|Elavon dispute reporting]] (id `1cltxFEklqGZgu-F3jJ3i3wvvIwPLOzHFUjUefJZuBas`) — op `append`, tab `PE Chargeback Log` — node "Append row in sheet3" (id `fd125896-1862-4a1e-95a0-3487df69b92a`)
- [[../resources/google-sheets/1cltxfeklqgzgu-f3jj3i3wvviwplozhfujuefjzubas|Elavon dispute reporting]] (id `1cltxFEklqGZgu-F3jJ3i3wvvIwPLOzHFUjUefJZuBas`) — op `?`, tab `Summary V2` — node "Get row(s) in sheet" (id `ffa39e78-cbe5-4b47-835c-9d9943cdd39a`)

### Sub-workflows (Execute Workflow calls)

- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'2" (id `23151017-febc-45d9-a314-c6b0ac82b316`)
- [[resolve-original-transaction|Resolve Original Transaction]] (n8n_id `VEpBuJNtK176eCyn`) — node "Call 'Resolve Original Transaction'" (id `4153bd49-05fc-476e-8f01-22176b267e96`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'1" (id `496ef260-f3f3-469e-8dd3-ea7bff9aa5dd`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'" (id `b01b3634-96c5-4f7e-a03f-013165495d04`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'" (id `edd491ac-6dfe-4aab-ab83-845a14a0a20a`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
