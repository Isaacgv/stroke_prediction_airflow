

import pymsteams

host ="http://localhost:8050/"
path_docs = "great_expectations/uncommitted/data_docs/local_site/validations/stroke_data/csv/warning/"

myTeamsMessage = pymsteams.connectorcard("https://epitafr.webhook.office.com/webhookb2/57c5a082-c81e-48cd-9b92-f7279598eedd@3534b3d7-316c-4bc9-9ede-605c860f49d2/IncomingWebhook/362046e3d3794351a42fa50fd8d80a02/5347364a-878b-4d50-810d-d18b7c79224e")


def send_alert(result):

    myMessageSection = pymsteams.cardsection()

    myTeamsMessage.title("Ingest Data Alert!")
    myTeamsMessage.text("Great expectation analysis")
    myMessageSection.addFact("Run Name:", result["run_name"])
    myMessageSection.addFact("Run Time:", result["run_time"])

    link_doc = host + path_docs + result["run_name"]+"/"+result["run_name"]+"/"+result["batch_id"]+".html"
    
    myTeamsMessage.addLinkButton("Information", link_doc)

    myTeamsMessage.addSection(myMessageSection)
    myTeamsMessage.color("#E7625F")

    myTeamsMessage.send()
