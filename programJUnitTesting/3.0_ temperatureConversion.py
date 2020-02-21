# To the Util Class add temperaturConversion static function, given the temperature in fahrenheit as input outputs the temperature in Celsius or viceversa using the formula
# -----------------Celsius to Fahrenheit:   (°C × 9/5) + 32 = °F
# ------------------Fahrenheit to Celsius:   (°F − 32) x 5/9 = °C
class temperatureConversion:
    def celsiusToFahrenheit(self,Celsius):
        return ((Celsius*(9/5))+32 )
    def faherenheitToCelsius(self, Faherenheit):
        print("Celsius C : ",(Faherenheit-32)*(5/9))
celsius=40
obj=temperatureConversion()
faherenheit=obj.celsiusToFahrenheit(celsius)
print("Faherenheit : ", faherenheit)
obj.faherenheitToCelsius(int(faherenheit))
