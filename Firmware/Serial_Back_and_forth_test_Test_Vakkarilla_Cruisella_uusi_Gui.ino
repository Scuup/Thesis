#include <SPI.h>
#include "mcp_can.h"


const int SPI_CS_PIN = 9;
MCP_CAN CAN(SPI_CS_PIN); 

int pin1 = 6;
int pin2 = 7;
char receivedChar = 0;
boolean newData = false;
boolean sendReq = false;
boolean speedCheckReq = false;

boolean plus = false;
boolean minus = false;

boolean volUp = false;
boolean volDown = false;

// HS2 music player vol +/-
unsigned char minusVol[8]={0xFE, 0xFF, 0xFF, 0xFF, 0x10, 0x0, 0x0, 0x0};
unsigned char minusVolEnd[8]={0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0, 0x0, 0x0};

unsigned char plusVol[8]={0xFD, 0xFF, 0xFF, 0xFF, 0x10, 0x0, 0x0, 0x0};
unsigned char plusVolEnd[8]={0xFD, 0xFF, 0xFF, 0xFF, 0x0, 0x0, 0x0, 0x0};

// HS2 Cruise Control +/-
unsigned char cruiseOnOff[8]={0x0, 0x20, 0x0, 0x0, 0x80, 0x92, 0x0, 0x0};
unsigned char cruiseMinus[8]={0x0, 0x20, 0x0, 0x10, 0x0, 0x92, 0x0, 0x0};
unsigned char cruisePlus[8]={0x0, 0x20, 0x0, 0x8, 0x0, 0x92, 0x0, 0x0};



void setup() {
    Serial.begin(115200);
    pinMode(pin1, OUTPUT);
    pinMode(pin2, OUTPUT);

    digitalWrite(pin1,LOW); // LOW = HS CAN / HIGH = FT CAN
    digitalWrite(pin2,HIGH); // LOW = FT CAN / HIGH = HS CAN
}

void loop() {
  serialRead();
  showData();
  chechStatus();
  sendCanData();
  checkSpeed();
  sendToCan();
}

// Check whether the serial buffer has something
void serialRead(){
  if (Serial.available()>0){
    receivedChar = Serial.read();
    newData = true;
    }
  }

//Show the received serial data to the end user, for debugging
void showData(){
  if(newData == true){
    Serial.print("I read the following from serial:");
    Serial.println(receivedChar);
    Serial.print("Following function performed:");
    newData = false;
    }
  }

// Status to check what should we do
void chechStatus(){
  switch(receivedChar){
    case 'a':
    sendReq = true;
    Serial.println("send data");
    receivedChar = 0;
    break;
       
    case 'b':
    sendReq = false;
    Serial.println("stop all");
    receivedChar = 0;
    break;

    case 'c':
    CAN.begin(CAN_500KBPS);
    Serial.println("set speed 500");
    receivedChar = 0;
    break;

    case 'd':
    CAN.begin(CAN_125KBPS);
    Serial.println("set speed 125");
    receivedChar = 0;
    break;

    case 'e':
    speedCheckReq = true;
    receivedChar = 0;
    break;

    case 'f':
    plus=true;
    //Serial.println("Plus");
    receivedChar = 0;
    break;

    case 'g':
    minus=true;
    //Serial.println("Minus");
    receivedChar = 0;
    break;

    case 'h':
    volUp=true;
    //Serial.println("Minus");
    receivedChar = 0;
    break;

    case 'i':
    volDown=true;
    //Serial.println("Minus");
    receivedChar = 0;
    break;

    default:
    //Serial.println("Check your input");
    break;
    
    }    
  }

// What we actually do when we know about the case
void sendCanData(){
  if (sendReq == true){
    unsigned char len = 0;
    unsigned char buf[8];
    
    if(CAN_MSGAVAIL == CAN.checkReceive()){            // check if data coming
        CAN.readMsgBuf(&len, buf);    // read data,  len: data length, buf: data buf
        unsigned long canId = CAN.getCanId();
        Serial.print(",");
        Serial.print(canId,HEX);
        Serial.print(",");
             
        for(int i = 0; i<len; i++)    // print the data
        {
            Serial.print(buf[i]); //Hexana lisää , HEX
            Serial.print(",");
        }
        Serial.println();
      }
    }
  }

void checkSpeed(){
  if (speedCheckReq == true){
    Serial.println("Starting to check the speed");
   
    // Test starts by setting the speed to 125 and checking if receive is ok, if not then next speed
    CAN.begin(CAN_125KBPS);
    delay(200);
    if(CAN_MSGAVAIL == CAN.checkReceive()){
      Serial.println("Tried 125KBPS, this migth be it, set speed to 125KBPS and test");
      }
    else{
      Serial.println("Tried 125KBPS, not it, I am changing to the next one");
      }

    // Test continues by setting the speed to 250 and checking if receive is ok, if not then next speed  
    CAN.begin(CAN_250KBPS);
    delay(200);
    
        if(CAN_MSGAVAIL == CAN.checkReceive()){
      Serial.println("Tried 250KBPS, this migth be it, set speed to 250KBPS and test");
      }
    else{
      Serial.println("Tried 250KBPS, not it, I am changing to the next one");
      }

    // Test continues by setting the speed to 500 and checking if receive is ok, if not then next speed
    CAN.begin(CAN_500KBPS);
    delay(200);
    
        if(CAN_MSGAVAIL == CAN.checkReceive()){
      Serial.println("Tried 500KBPS, this migth be it, set speed to 500KBPS and test");
      }
    else{
      Serial.println("Tried 500KBPS, not it, I am changing to the next one");
      }
    
    }
    speedCheckReq = false;
  }

//unsigned char stmp[8]={254, 0, 0, 0, 10, 0, 0, 0};
//unsigned char stmp2[8]={0xFD, 0x0, 0x0, 0x0, 0x10, 0x0, 0x0, 0x0};

void sendToCan(){
  if (plus == true){
    Serial.println("Cruise / Plussataan");
    CAN.sendMsgBuf(0x83, 0, 8, cruisePlus);
//    delay(100);
//    CAN.sendMsgBuf(0x83, 0, 8, cruisePlus);
//    delay(10);
    
    //CAN.sendMsgBuf(0x2a1, 0, 8, plusVolEnd);
    }
   else if (minus == true){
    Serial.println("Cruise / Miinusta");
    CAN.sendMsgBuf(0x83, 0, 8, cruiseMinus);
    //CAN.sendMsgBuf(0x2a1, 0, 8, minusVolEnd);
    }

    else if (volDown == true){
    Serial.println("Radio / Miinusta");
    CAN.sendMsgBuf(0x2a1, 0, 8, minusVol);
    CAN.sendMsgBuf(0x2a1, 0, 8, minusVolEnd);
    }

    else if (volUp == true){
    Serial.println("Radio / plussaa");
    CAN.sendMsgBuf(0x2a1, 0, 8, plusVol);
    CAN.sendMsgBuf(0x2a1, 0, 8, plusVolEnd);
    }
  volUp=false;
  volDown=false;
  plus=false;
  minus=false;
  }
