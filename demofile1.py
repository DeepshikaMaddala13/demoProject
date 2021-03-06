journal_col_names=["setOfBooksId", "ledgerId", "groupId", "userJeCategoryName", "userJeSourceName", "accountingDate", "currencyCode",
                   "actualFlag", "segment1", "segment2", "segment3", "segment4", "segment5", "segment6", "segment7", "debitAmount", "creditAmount",
                   "reference1", "reference4", "journalDescription", "createdBy", "periodName", "fileId", "conversionDate","conversiontype",
                   "precision", "lastUpdatedBy", "fileStatus", "status", "dateCreated", "codeCombinationId", "segment8", "segment9", "segment10", "encumbranceTypeId",
                   "budgetVersionId", "currencyConversionRate", "accountedDebitAmount", "accountedCreditAmount", "reference2", "reference3", "reference5",
                   "reference6", "reference7", "reference8", "reference9", "statAmount", "ussglTransactionCode", "attribute1", "attribute2", "attribute3",
                   "attribute4", "attribute5", "attribute6", "attribute7", "attribute8", "attribute9", "attribute10", "context", "context1", "context2",
                   "context3", "invoiceAmount", "invoiceIdentifier", "taxCode", "loadRequestId", "descrFlexErrorMessage", "functionalCurrenCode", "glBatchId",
                   "jeBatchId", "jeHeaderId", "rowId", "subledgerDocSequenceId", "subledgerDocSequenceValue", "chartOfAccountsId", "warningCode", "creationDate",
                   "lastUpdateDate", "lastUpdateLogin", "reference21", "reference22", "reference23", "reference24", "reference25", "reference26", "reference27",
                   "reference28", "reference29", "reference30", "ledgerName", "filePath", "amzReference1"]
names=['SET_OF_BOOKS_ID','LEDGER_ID', 'GROUP_ID', 'USER_JE_CATEGORY_NAME', 'USER_JE_SOURCE_NAME', 'ACCOUNTING_DATE', 'CURRENCY_CODE', 'ACTUAL_FLAG'
    , 'SEGMENT1', 'SEGMENT2', 'SEGMENT3', 'SEGMENT4', 'SEGMENT5', 'SEGMENT6', 'SEGMENT7', 'entered_dr', 'entered_cr', 'REFERENCE1', 'REFERENCE4', 'REFERENCE10'
    , 'created_by', 'period_name' , 'file_id', 'currency_conversion_date', 'user_currency_conversion_type', 'precision', 'last_updated_by'
    , 'file_status' , 'status', 'date_created', 'code_combination_id','segment8', 'segment9' , 'segment10' , 'encumbrance_type_id', 'budget_version_id'
    , 'currency_conversion_rate' , 'accounted_dr', 'accounted_cr', 'REFERENCE2', 'REFERENCE3', 'REFERENCE5', 'REFERENCE6', 'REFERENCE7'
    , 'REFERENCE8' , 'REFERENCE9', 'stat_amount', 'ussgl_transaction_code', 'ATTRIBUTE1', 'ATTRIBUTE2', 'ATTRIBUTE3', 'ATTRIBUTE4', 'ATTRIBUTE5'
    , 'ATTRIBUTE6', 'ATTRIBUTE7', 'ATTRIBUTE8', 'ATTRIBUTE9', 'ATTRIBUTE10', 'CONTEXT', 'CONTEXT1', 'CONTEXT2', 'CONTEXT3', 'invoice_amount' , 'invoice_identifier'
    , 'tax_code', 'load_request_id', 'descr_flex_error_message', 'functional_currency_code', 'gl_batch_id', 'je_batch_id', 'je_header_id'
    , 'je_line_num', 'subledger_doc_sequence_id', 'subledger_doc_sequence_value', 'chart_of_accounts_id', 'warning_code', 'creation_date'
    , 'last_update_date', 'last_update_login', 'REFERENCE21', 'REFERENCE22', 'REFERENCE23', 'REFERENCE24', 'REFERENCE25', 'REFERENCE26', 'REFERENCE27'
    , 'REFERENCE28', 'REFERENCE29', 'REFERENCE30', 'ledger_name','file_path', 'amz_reference1']
print(len(journal_col_names),len(names))
for (i,j) in zip(journal_col_names,names):
    print('"'+i+'":"'+j+'"'+',')
