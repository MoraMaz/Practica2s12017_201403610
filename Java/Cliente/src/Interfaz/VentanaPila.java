package Interfaz;

import PythonConexion.PythonConexion;
import javax.swing.JOptionPane;

/**
 *
 * @author moramaz
 */
public class VentanaPila extends javax.swing.JFrame {

    private final PythonConexion conexion;
    
    public VentanaPila(PythonConexion conexion) {
        initComponents();
        setLocationRelativeTo(null);
        this.conexion = conexion;
    }
    
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        btnPop = new javax.swing.JButton();
        btnPush = new javax.swing.JButton();
        txtPush = new javax.swing.JTextField();

        btnPop.setText("Pop");
        btnPop.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnPopActionPerformed(evt);
            }
        });

        btnPush.setText("Push");
        btnPush.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnPushActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap(41, Short.MAX_VALUE)
                .addComponent(txtPush, javax.swing.GroupLayout.PREFERRED_SIZE, 244, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(25, 25, 25))
            .addGroup(layout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                    .addComponent(btnPush, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(btnPop, javax.swing.GroupLayout.DEFAULT_SIZE, 88, Short.MAX_VALUE))
                .addGap(0, 0, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addContainerGap(147, Short.MAX_VALUE)
                .addComponent(txtPush, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(btnPush)
                .addGap(31, 31, 31)
                .addComponent(btnPop)
                .addGap(130, 130, 130))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnPushActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnPushActionPerformed
        if(txtPush.getText().matches("\\d+")){
            conexion.stak_add(txtPush.getText());
        }else{
            JOptionPane.showMessageDialog(this, "Sólo se pueden ingresar números.");
        }
        txtPush.setText("");
    }//GEN-LAST:event_btnPushActionPerformed

    private void btnPopActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnPopActionPerformed
        conexion.stak_remove();
    }//GEN-LAST:event_btnPopActionPerformed

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnPop;
    private javax.swing.JButton btnPush;
    private javax.swing.JTextField txtPush;
    // End of variables declaration//GEN-END:variables
}