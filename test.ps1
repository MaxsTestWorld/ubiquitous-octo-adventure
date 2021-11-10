
[CmdletBinding()]
Param(
    [ValidateScript({$_ -like "*@education.gov.uk"})]
    [Parameter(Mandatory = $true)]
    [String[]]$EmailAddressArray
)

$EmailAddress = 'Niall.GERAGHTY@education.gov.uk' , 'synduja.ravendrakumar@education.gov.uk' , 'nicholas.grounds@education.gov.uk'
foreach ($EmailAddress in $EmailAddressArray) {
    Write-Output "  -> Generating email to $EmailAddress"
}