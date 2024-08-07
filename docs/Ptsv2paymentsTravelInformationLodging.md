# Ptsv2paymentsTravelInformationLodging

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_in_date** | **str** | Date on which the guest checked in. In the case of a no-show or a reservation, the scheduled arrival date. Format: &#x60;MMDDYY&#x60;. For best interchange rates, make sure it is a valid date.  | [optional] 
**check_out_date** | **str** | Date on which the guest checked out. Format: &#x60;MMDDYY&#x60;. For best interchange rates, make sure it is a valid date.  | [optional] 
**room** | [**list[Ptsv2paymentsTravelInformationLodgingRoom]**](Ptsv2paymentsTravelInformationLodgingRoom.md) | The object containing the number of nights and the daily rate that applies for that no of nights.  | [optional] 
**smoking_preference** | **str** | Smoking preference of the guest. Possible values: - &#x60;Y&#x60;: smoking room - &#x60;N&#x60;: non-smoking room  | [optional] 
**number_of_rooms** | **int** | Number of rooms booked by the cardholder.  | [optional] 
**number_of_guests** | **int** | Number of guests staying in the room.  | [optional] 
**room_bed_type** | **str** | Type of room, such as queen, king, or two doubles.  | [optional] 
**room_tax_type** | **str** | Type of tax, such as tourist or hotel.  | [optional] 
**room_rate_type** | **str** | Type of rate, such as corporate or senior citizen.  | [optional] 
**guest_name** | **str** | Name of the guest under which the room is reserved.  | [optional] 
**customer_service_phone_number** | **str** | Your toll-free customer service phone number.  | [optional] 
**corporate_client_code** | **str** | Code assigned to a business. You can use this code to identify corporate rates and discounts for guests.  | [optional] 
**additional_discount_amount** | **str** | Amount of an additional coupon or discount.  | [optional] 
**room_location** | **str** | Location of room, such as lake view or ocean view.  | [optional] 
**special_program_code** | **str** | Code that identifies special circumstances. Possible values: - &#x60;1&#x60;: lodging (default) - &#x60;2&#x60;: no show reservation - &#x60;3&#x60;: advanced deposit  | [optional] 
**total_tax_amount** | **str** | Total tax amount.  | [optional] 
**prepaid_cost** | **str** | Prepaid amount, such as a deposit.  | [optional] 
**food_and_beverage_cost** | **str** | Cost for all food and beverages.  | [optional] 
**room_tax_amount** | **str** | Total tax for the room.  | [optional] 
**adjustment_amount** | **str** | Adjusted amount charged in addition to the reservation amount after the stay is complete.  | [optional] 
**phone_cost** | **str** | Cost of telephone services.  | [optional] 
**restaurant_cost** | **str** | Cost of restaurant purchases  | [optional] 
**room_service_cost** | **str** | Cost of room service.  | [optional] 
**mini_bar_cost** | **str** | Cost of mini-bar purchases.  | [optional] 
**laundry_cost** | **str** | Cost of laundry services.  | [optional] 
**miscellaneous_cost** | **str** | Miscellaneous costs.  | [optional] 
**gift_shop_cost** | **str** | Cost of gift shop purchases.  | [optional] 
**movie_cost** | **str** | Cost of movies.  | [optional] 
**health_club_cost** | **str** | Cost of health club services.  | [optional] 
**valet_parking_cost** | **str** | Cost of valet parking services.  | [optional] 
**cash_disbursement_cost** | **str** | Cost of the cash that was disbursed plus any associated service fees  | [optional] 
**non_room_cost** | **str** | Cost of non-room purchases, such as meals and gifts.  | [optional] 
**business_center_cost** | **str** | Cost of business center services.  | [optional] 
**lounge_bar_cost** | **str** | Cost of lounge and bar purchases.  | [optional] 
**transportation_cost** | **str** | Cost of transportation services.  | [optional] 
**gratuity_amount** | **str** | Gratuity.  | [optional] 
**conference_room_cost** | **str** | Cost of conference room services.  | [optional] 
**audio_visual_cost** | **str** | Cost of audio visual services.  | [optional] 
**banquest_cost** | **str** | Cost of banquet services.  | [optional] 
**non_room_tax_amount** | **str** | Tax on non-room purchases.  | [optional] 
**early_check_out_cost** | **str** | Service fee for early departure.  | [optional] 
**internet_access_cost** | **str** | Cost of Internet access.  | [optional] 
**name** | **str** | Name of the hotel for which the reservation is for. Mandatory in case the merchant&#39;s business type is Hotel.  | [optional] 
**hotel_name** | **str** | The name of the hotel for which the reservation was made.  | [optional] 
**check_in_date_time** | **str** | The date of the check-in in GMT+8 offset.  | [optional] 
**check_out_date_time** | **str** | The date of the check-out in GMT+8 offset.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


