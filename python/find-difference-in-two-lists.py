#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python code t get difference of two lists

def diff(li1, li2):
    return list(set(li1) - set(li2))


# Driver Code

# li1 = [
#     'Denmark',
#     'Netherlands',
#     'China',
#     'Hong Kong',
#     'India',
#     'Oman',
#     'Bahrain',
#     'Pakistan',
#     'Egypt',
#     'Saudi Arabia',
#     'Bangladesh',
#     'United Arab Emirates',
#     'Sri Lanka',
#     'Jordan',
#     'Kuwait',
#     'Lebanon',
#     'Iraq',
#     'Qatar',
#     'Singapore',
#     'New Zealand',
#     'Indonesia',
#     'Cambodia',
#     'Thailand',
#     'Vietnam',
#     'Australia',
#     'Philippines',
#     'Malaysia',
#     'Taiwan',
#     'Japan',
#     'South Korea',
#     'Peru',
#     'Colombia',
#     'Brazil',
#     'Ecuador',
#     'Chile',
#     'Argentina',
#     'Uruguay',
#     'Guatemala',
#     'Honduras',
#     'Mexico',
#     'El Salvador',
#     'Costa Rica',
#     'Dominican Republic',
#     'Panama',
#     'Trinidad and Tobago',
#     'Sweden',
#     'Latvia',
#     'Belarus',
#     'Great Britain',
#     'Russia',
#     'Lithuania',
#     'Estonia',
#     'Finland',
#     'Norway',
#     'Ireland',
#     'Belgium',
#     'Czech Republic',
#     'Germany',
#     'Poland',
#     'Slovakia',
#     'Hungary',
#     'Switzerland',
#     'Austria',
#     'Morocco',
#     'Spain',
#     'France',
#     'Portugal',
#     'Algeria',
#     'Tunisia',
#     'Italy',
#     'Ukraine',
#     'Georgia',
#     'Turkey',
#     'Bulgaria',
#     'Israel',
#     'Slovenia',
#     'Croatia',
#     'Romania',
#     'Cyprus',
#     'Greece',
#     'Mauritius',
#     'Madagascar',
#     'Namibia',
#     'South Africa',
#     'Mozambique',
#     'Malawi',
#     'Zambia',
#     'Tanzania',
#     'Kenya',
#     'Uganda',
#     'Lesotho',
#     'Swaziland',
#     'Zimbabwe',
#     'Botswana',
#     'Liberia',
#     'Sierra Leone',
#     'Angola',
#     'USA',
#     'Canada',
#     'Benin',
#     'Niger',
#     'Cameroon',
#     'Gabon',
#     'Congo',
#     'Republic of the Congo',
#     'Sudan',
#     'Ethiopia',
#     'Gambia',
#     'Ghana',
#     'Guinea',
#     'Burkina Faso',
#     'Ivory Coast',
#     'Mali',
#     'Mauritania',
#     'Nigeria',
#     'Senegal',
#     'Guinea-Bissau',
#     'Togo',
#     'Bahamas',
#     'Bermuda',
#     'Brunei',
#     'Cape Verde',
#     'Myanmar',
#     'Bolivia',
#     'Iran',
#     'Nicaragua',
#     'Barbados',
#     'British Virgin Islands',
#     'Papua New Guinea',
#     'Djibouti',
#     'Haiti',
#     'Venezuela',
#     ]
# li2 = [
#     'India',
#     'Switzerland',
#     'Saudi Arabia',
#     'United Arab Emirates',
#     'New Zealand',
#     'Philippines',
#     'Nigeria',
#     'China',
#     'Ghana',
#     'Indonesia',
#     'Brazil',
#     'Japan',
#     'Sweden',
#     'South Africa',
#     'Belgium',
#     'Oman',
#     'Bahrain',
#     'Qatar',
#     'Denmark',
#     'Czech Republic',
#     'Turkey',
#     'Australia',
#     'Canada',
#     'Germany',
#     'Malaysia',
#     'Netherlands',
#     'Singapore',
#     'Tanzania',
#     'Kenya',
#     'Hungary',
#     'Hong Kong',
#     'South Korea',
#     'Finland',
#     'Austria',
#     'Mauritius',
#     'Peru',
#     'Spain',
#     'Mexico',
#     'Senegal',
#     'Egypt',
#     'Norway',
#     'Poland',
#     'Dominican Republic',
#     'Argentina',
#     'Lebanon',
#     'Bangladesh',
#     'Russia',
#     'Portugal',
#     'Israel',
#     'Bolivia',
#     'Costa Rica',
#     'Ecuador',
#     'Ethiopia',
#     'Guatemala',
#     'Niger',
#     'Zambia',
#     'Malawi',
#     'Gabon',
#     'France',
#     'Congo',
#     'Thailand',
#     'Italy',
#     'Uganda',
#     'Ireland',
#     'Kuwait',
#     'Panama',
#     'Vietnam',
#     'Algeria',
#     'Bulgaria',
#     'Colombia',
#     'Greece',
#     'Iraq',
#     'Morocco',
#     'Myanmar',
#     'Pakistan',
#     'Sri Lanka',
#     'Taiwan',
#     'Romania',
#     'Chile',
#     'Cyprus',
#     'Zimbabwe',
#     'Mozambique',
#     'Bermuda',
#     'Ukraine',
#     'Lithuania',
#     'Slovakia',
#     'Jordan',
#     'Angola',
#     'Bahamas',
#     'Benin',
#     'Cambodia',
#     'Cameroon',
#     'Gambia',
#     'Georgia',
#     'Guinea',
#     'Guinea-Bissau',
#     'Latvia',
#     'Liberia',
#     'Madagascar',
#     'Mauritania',
#     'Namibia',
#     'Papua New Guinea',
#     'Sierra Leone',
#     'Slovenia',
#     'Sudan',
#     'Togo',
#     'Tunisia',
#     'Croatia',
#     'El Salvador',
#     'Estonia',
#     'Honduras',
#     'Nicaragua',
#     'Trinidad and Tobago',
#     'Uruguay',
#     'Venezuela',
#     'Barbados',
#     'Belarus',
#     'British Virgin Islands',
#     'Brunei',
#     'Burkina Faso',
#     'Cape Verde',
#     'Djibouti',
#     'Haiti',
#     'Lesotho',
#     'Mali',
#     'Swaziland',
#     ]
# print diff(li1, li2)
