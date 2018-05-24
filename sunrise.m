data = dlmread('model/data.txt');

samples = [ data(:,1) data(:,2)+data(:,3)/60 data(:,4)+data(:,5)/60  ];

stairs(samples(:,2));
hold on; box on; grid on;
stairs(samples(:,3));
legend('wschód', 'zachód');
xlabel('próbka')
ylabel('godzina dnia')