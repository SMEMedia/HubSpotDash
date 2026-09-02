# HubSpot Email Performance Dashboard

This dashboard gives the marketing team one place to review HubSpot marketing-email performance. It reads reporting information but does not send emails, edit campaigns, or change HubSpot records.

## Important links

- [Open the Email Dashboard](https://smeemaildash.streamlit.app/)
- [Shared saved-data Sheet](https://docs.google.com/spreadsheets/d/1IHIwO8fI2KG0_d8yuZ12Rai4QSjPcJ0_de7zLmuPZ4g/edit)
- [SMEMedia repository](https://github.com/SMEMedia/HubSpotDash)

## Use the dashboard

1. Choose the reporting period and email type.
2. Leave **Use local cache when available** selected for normal use.
3. Select **Refresh from HubSpot** when the newest available information is needed.
4. Review:
   - **Overview** for results by email type.
   - **Trends** for changes over time.
   - **Top Links** for the most-clicked destinations.
   - **Keywords** for wording and engagement comparisons.
   - **Email Detail** for individual messages.

The **Last refresh** message shows when the saved information was updated. A refresh may take several minutes.

## How email categories work

The dashboard groups messages using their HubSpot names. Newsletter names such as **MW m/d/yy** and advertising names such as **Company Custom Email** are recognized. Messages that do not match an established pattern may appear as **Unclassified**.

## Troubleshooting

### The information is old

- Check **Last refresh**.
- Confirm the desired reporting period.
- Select **Refresh from HubSpot** once and wait for completion.
- If the refresh fails, leave the cache option selected so the team can continue viewing the last successful copy.

### A token, credential, or permissions error appears

- Do not paste a credential into the dashboard or share it in email, chat, GitHub, or a screenshot.
- Ask the HubSpot administrator to confirm that the dashboard service key is active and can read marketing-email information.
- Ask the Streamlit owner to update the saved secret if the key was rotated.
- After the correction, refresh once and confirm **Last refresh** changes.

### Google Sheets reports an error

- The dashboard may continue using its last saved backup.
- Confirm the shared Sheet still exists.
- Ask the Google Workspace owner to confirm the dashboard account can edit it.
- Ask the Streamlit owner to verify the saved Google connection.

### An email is Unclassified or under the wrong type

- Check the email name in HubSpot.
- Compare it with the established naming pattern.
- If the name is correct, send the exact email name and expected category to technical support.

### Results differ from HubSpot

- Confirm the same date range and email population are being compared.
- Refresh the dashboard before escalating.
- Remember that opens and clicks can continue to change after an email is sent.
- Record the dashboard value, HubSpot value, email name, date range, and comparison time.

### The dashboard does not open

- Confirm the live link above is being used.
- Refresh the browser once or try a private window.
- Check [Streamlit Community Cloud](https://share.streamlit.io/) for an app status message.
- Send the visible error and approximate time to the Streamlit owner.

## Ongoing maintenance

- Refresh only when current HubSpot information is needed; use the saved copy for normal review.
- Keep HubSpot, Google Sheet, Streamlit, and repository access assigned to current SME staff.
- Review service-key ownership and permissions periodically.
- Escalate credential, permission, naming-rule, or deployment changes to the assigned technical owner.
