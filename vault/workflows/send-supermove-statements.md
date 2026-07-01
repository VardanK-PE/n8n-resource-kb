---
n8n_id: "du7j1kACkcXyYnvY"
name: "Send Supermove Statements"
status: active
last_modified: 2026-05-27T19:58:47.495Z
tags: []
fingerprint: "dbed69659a90a95d73182fcc666bcdb6682bea96413c74c5bea527964da5dd87"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Send Supermove Statements

## Summary

- **Status:** active
- **n8n ID:** `du7j1kACkcXyYnvY`
- **Nodes:** 47
- **Last modified:** 2026-05-27T19:58:47.495Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `03609e67-175c-4a48-87d9-e1f948b03d4b`)
- **schedule** — node "Schedule Trigger" (id `770e801c-4203-459c-8a7d-17ad79f8969a`) — `every 1 month(s) on day 2`
- **manual** — node "When clicking ‘Execute workflow’" (id `87a395fb-ad6a-47c1-b380-9940ea76d641`)

## Depends on

### Credentials

- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "HTTP Request" (id `032ffaf0-f583-4376-bafe-daa7054f282d`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Send a message2" (id `0fc38780-746a-41fe-a337-012a04e53878`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message3" (id `11224b17-157d-40f5-909e-17b26f3fa27d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `25b40ce6-7f8a-45d6-b139-7388f9c0adcf`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet1" (id `27445fbd-492a-418d-9f1d-f61dffe40e1d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `2be98359-6ffb-4750-9914-3dafd4aaefe9`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message1" (id `84bea903-2c67-4283-bf12-4c84017de594`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `8d7a4666-7b51-422a-bec2-c014c7e1e578`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Resolve Statement File URL" (id `dec57477-1d74-4932-b66e-d9069bf09d1c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `fd1a52af-3725-4e2f-bdba-d3656a50d6f0`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `ff9df867-3225-439e-928e-79eed26e83de`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/merchant/{{ $json['Merchant ID'] }}/statements?page=1` — node "HTTP Request" (id `032ffaf0-f583-4376-bafe-daa7054f282d`)
- *(dynamic URL)* — `GET {{ $json.fileUrl }}` — node "Download the statement" (id `ca86647b-bc30-4c6e-a1f4-489b1a28ec1b`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/merchant/{{ $('Workflow Entry').item.json['Merchant ID'] }}/statements/{{$json.id}}/view` — node "Resolve Statement File URL" (id `dec57477-1d74-4932-b66e-d9069bf09d1c`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `ff9df867-3225-439e-928e-79eed26e83de`)

### Google Sheets

- [[../resources/google-sheets/1e09p28gzimo4lzju-vqj9igixy3qahnsvcbofzv2h-a|SuperMove Datastore]] (id `1e09P28gzIMO4lzjU-VQJ9iGIxy3QaHNsvcbOfzV2H_A`) — op `?`, tab `Statements Data` — node "Get row(s) in sheet" (id `25b40ce6-7f8a-45d6-b139-7388f9c0adcf`)
- [[../resources/google-sheets/1e09p28gzimo4lzju-vqj9igixy3qahnsvcbofzv2h-a|SuperMove Datastore]] (id `1e09P28gzIMO4lzjU-VQJ9iGIxy3QaHNsvcbOfzV2H_A`) — op `appendOrUpdate`, tab `Statements Data` — node "Append or update row in sheet1" (id `27445fbd-492a-418d-9f1d-f61dffe40e1d`)
- [[../resources/google-sheets/1e09p28gzimo4lzju-vqj9igixy3qahnsvcbofzv2h-a|SuperMove Datastore]] (id `1e09P28gzIMO4lzjU-VQJ9iGIxy3QaHNsvcbOfzV2H_A`) — op `appendOrUpdate`, tab `Statements Data` — node "Append or update row in sheet" (id `2be98359-6ffb-4750-9914-3dafd4aaefe9`)

### Slack channels

- [[../resources/slack-channels/c042mgb19m2|ops-internal]] (id `C042MGB19M2`) — op `channel` — node "Send a message3" (id `11224b17-157d-40f5-909e-17b26f3fa27d`)
- [[../resources/slack-channels/c042mgb19m2|ops-internal]] (id `C042MGB19M2`) — op `channel` — node "Send a message1" (id `84bea903-2c67-4283-bf12-4c84017de594`)
- [[../resources/slack-channels/c042mgb19m2|ops-internal]] (id `C042MGB19M2`) — op `channel` — node "Send a message4" (id `fd1a52af-3725-4e2f-bdba-d3656a50d6f0`)

### Sub-workflows (Execute Workflow calls)

- [[send-supermove-statements|Send Supermove Statements]] (n8n_id `du7j1kACkcXyYnvY`) — node "Call 'Send Supermove Statements'" (id `0bedd787-69ec-4f2a-9e25-6c089cbc1ffe`)

## Used by (workflows)

- [[send-supermove-statements|Send Supermove Statements]] — node "Call 'Send Supermove Statements'" (id `0bedd787-69ec-4f2a-9e25-6c089cbc1ffe`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
