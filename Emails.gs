function getSpecificSpreadsheetByName() {
  // Replace with your spreadsheet name
  const spreadsheetName = "2025test";
  // Get all spreadsheets with the given name
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(spreadsheetName);
    // Log the sheet name
  Logger.log("Sheet Name: " + sheet.getName());
  return sheet
}

function sendEmailsFromSheet() {
  // Open the Google Sheet by its ID or name
  const sheet = getSpecificSpreadsheetByName();
  // Get the data range of the sheet
  const dataRange = sheet.getDataRange();

  // Get the values from the sheet as a 2D array
  const data = dataRange.getValues();

  // Loop through each row of the sheet (skip the header row)
  for (let i = 0; i < data.length; i++) {
    const row = data[i];

    // Extract the email, subject, and message from the row
    const emailAddress = row[0]; // First column (A) contains the email address
    const subject = row[1];     // Second column (B) contains the subject
    const message = row[2];      // Third column (C) contains the message body

    const body = `Hello ${message},\n\nYour email is ${emailAddress}, and your current ID is ${subject}.\n\nThank you!`;



    // Check if the email address is not empty
    if (emailAddress) {
      try {
        // Send the email
        GmailApp.sendEmail(emailAddress, subject, body);

        // Log the sent email
        Logger.log(`Email sent to: ${emailAddress}`);

        // Mark the row as "Sent" (optional)
        sheet.getRange(i + 1, 4).setValue("Sent"); // Fourth column (D) for status
      } catch (e) {
        // Log any errors
        Logger.log(`Failed to send email to: ${emailAddress}. Error: ${e.toString()}`);

        // Mark the row as "Failed" (optional)
        sheet.getRange(i + 1, 4).setValue("Failed");
      }
    }
  }
}